#
# MIT License
#
# Copyright (c) 2020 Pablo Rodriguez Nava, @pablintino
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#


import base64
import binascii
import logging

from app import db
from models import FootprintReference, LibraryReference
from models.internal.internal_models import StorableLibraryResourceType, StorageStatus
from services import storage_service
from services.exceptions import ResourceAlreadyExistsApiError, ResourceNotFoundApiError, InvalidFootprintApiError, \
    InvalidSymbolApiError, InvalidStorableTypeError
from tasks import rq_helpers
from utils import parse_olefile_library, LibType

__logger = logging.getLogger(__name__)


def __validate_storable_type(storable_type):
    if storable_type != StorableLibraryResourceType.FOOTPRINT and storable_type != StorableLibraryResourceType.SYMBOL:
        raise InvalidStorableTypeError(f'The given storable type is not expected. Given type: {storable_type.value}')


def __get_error_for_type(storable_type):
    __validate_storable_type(storable_type)
    return InvalidFootprintApiError if storable_type == StorableLibraryResourceType.FOOTPRINT else InvalidSymbolApiError


def __get_model_for_storable_type(storable_type):
    __validate_storable_type(storable_type)
    return FootprintReference if storable_type == StorableLibraryResourceType.FOOTPRINT else LibraryReference


def __get_library(expected_type, encoded_data):
    if encoded_data:
        try:
            # Parse the given data
            decoded_data = base64.b64decode(encoded_data)
            lib = parse_olefile_library(decoded_data)

            # Be sure that the encoded data is of the expected type
            if (expected_type == StorableLibraryResourceType.SYMBOL and lib.lib_type != LibType.SCH) or (
                    expected_type == StorableLibraryResourceType.FOOTPRINT and lib.lib_type != LibType.PCB):
                raise __get_error_for_type(expected_type)(
                    'The given encoded data is not of the expected type. {expected_type=' +
                    (LibType.SCH.value if expected_type == StorableLibraryResourceType.SYMBOL else LibType.PCB.value) +
                    ', actual_type=' + lib.lib_type.value + '}')

            return lib
        except binascii.Error:
            raise __get_error_for_type(expected_type)('Invalid base64 encoded data. Incorrect padding')
        except IOError as err:
            raise __get_error_for_type(expected_type)(f'The given Altium file is corrupt',
                                                      err.args[0] if len(err.args) > 0 else None)
    else:
        raise __get_error_for_type(expected_type)('Encoded library data not provided')


def __update_model_reference(storable_type, model, new_reference):
    exists = (db.session.query(LibraryReference.id).filter_by(symbol_path=model.get_file_path(),
                                                              symbol_ref=new_reference).scalar()
              if storable_type == StorableLibraryResourceType.SYMBOL else db.session.query(
        FootprintReference.id).filter_by(footprint_path=model.get_file_path(),
                                         footprint_ref=new_reference).scalar()) is not None

    if not exists:
        model.set_reference(new_reference)
        db.session.add(model)
        db.session.commit()
    else:
        raise ResourceAlreadyExistsApiError(
            f'The given {storable_type.value} already exists. Path: {model.get_file_path()} Reference: {new_reference}')


def update_object_data(storable_type, model_id, encoded_data):
    model = __get_model_for_storable_type(storable_type).query.get(model_id)
    if model is None:
        msg = 'The requested ' + storable_type.value + ' cannot be found. {id=' + str(model_id) + '}'
        __logger.debug(msg)
        raise ResourceNotFoundApiError(msg, missing_id=model_id)
    else:

        current_encoded_data = storage_service.get_encoded_file_from_repo(model)
        if encoded_data == current_encoded_data:
            __logger.debug('Given new storable object data has the same content as the current one. Skipping...')
            return

        lib = __get_library(storable_type, encoded_data)

        if lib.part_exists(model.get_reference()):
            # Simple update of the library, no database changes needed
            __logger.debug(
                'Updating storable object data without reference update. {storable_type=' + storable_type.value +
                ', reference=' + model.get_reference() + ', model_id=' + str(model_id) + '}')
        elif lib.count == 1:
            # Update reference and if success change data in repo
            new_reference = lib.parts[next(iter(lib.parts.keys()))].name
            __logger.debug(
                'Updating storable object data and reference. {storable_type=' + storable_type.value +
                ', new_reference=' + new_reference + ', old_reference=' + model.get_reference() + ', model_id=' + str(
                    model_id) + '}')
            __update_model_reference(storable_type, model, new_reference)
        else:
            # Cannot update the library file
            raise __get_error_for_type(storable_type)(
                f'The given {storable_type.value} file cannot be updated without {storable_type.value} reference changes')

        # Reset storage status
        model.storage_status = StorageStatus.NOT_STORED
        db.session.add(model)
        db.session.commit()

        # Signal background process to store the storable object
        rq_helpers.launch_storage_task(storable_type, model.id, encoded_data)


def create_storable_library_object(storable_type, reference_name, storable_path, description, encoded_data):
    __validate_storable_type(storable_type)

    # Parse storable object from encoded data and check its content
    lib = __get_library(storable_type, encoded_data)

    # Verify that the body contains enough information
    if not reference_name:
        # Try to obtain the reference from the library data
        if lib.count != 1:
            raise __get_error_for_type(storable_type)(
                f'More than one part in the given {lib.lib_type.value} library. Provide a reference')
        else:
            reference_name = lib.parts[next(iter(lib.parts.keys()))].name

    # If check that the given reference exists
    if not lib.part_exists(reference_name):
        raise __get_error_for_type(storable_type)(
            f'The given reference {reference_name} does not exist in the given library')

    # If no description is provided try to populate it from library data
    if not description:
        description = lib.parts[reference_name].description

    __logger.debug('Creating a new storable object. {storable_type=' + storable_type.value +
                   ', reference_name=' + reference_name + ', storable_path=' + storable_path +
                   ', description=' + description + '}')

    exists_id = db.session.query(LibraryReference.id).filter_by(symbol_path=storable_path,
                                                                symbol_ref=reference_name).scalar() \
        if storable_type == StorableLibraryResourceType.SYMBOL else db.session.query(
        FootprintReference.id).filter_by(
        footprint_path=storable_path, footprint_ref=reference_name).scalar()

    if not exists_id:

        # Create a model based on the storable object type
        model = FootprintReference(footprint_path=storable_path, footprint_ref=reference_name,
                                   description=description) if storable_type == StorableLibraryResourceType.FOOTPRINT \
            else LibraryReference(symbol_path=storable_path, symbol_ref=reference_name, description=description)

        # Ensure that storage status at creation time is set to NOT_STORED
        model.storage_status = StorageStatus.NOT_STORED

        db.session.add(model)
        db.session.commit()
        __logger.debug('Storable object created. {id=' + str(model.id) + '}')

        # Signal background process to store the object
        rq_helpers.launch_storage_task(storable_type, model.id, encoded_data)

        return model
    else:
        msg = 'Cannot create the requested storable object cause it already exists. {storable_type=' + \
              storable_type.value + ', reference_name=' + reference_name + ', storable_path=' + storable_path + '}'
        __logger.warning(msg)
        raise ResourceAlreadyExistsApiError(msg=msg, conflicting_id=exists_id)


def get_storable_model(storable_type, model_id):
    __logger.debug(
        'Retrieving a storable object. {storable_type=' + storable_type.value + ', model_id=' + str(model_id) + '}')
    model = __get_model_for_storable_type(storable_type).query.get(model_id)
    if model is None:
        msg = 'Storable object not found. {storable_type=' + storable_type.value + ', model_id=' + str(model_id) + '}'
        __logger.debug(msg)
        raise ResourceNotFoundApiError(msg, missing_id=model_id)
    else:
        return model
