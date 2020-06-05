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
from models import FootprintReference
from models.internal.internal_models import StorageResourceType, StorageStatus
from services.exceptions import ResourceAlreadyExistsApiError, ResourceNotFoundApiError, InvalidFootprintApiError
from utils import parse_olefile_library, LibType
from tasks import rq_helpers

__logger = logging.getLogger(__name__)


def __get_library(footprint_dto):
    # If binary is provided try to parse it
    if footprint_dto.encoded_data:
        try:
            # Parse the given data
            decoded_data = base64.b64decode(footprint_dto.encoded_data)
            lib = parse_olefile_library(decoded_data)

            # Be sure that a PCB Library has been provided
            if lib.lib_type != LibType.PCB:
                raise InvalidFootprintApiError(f'The given encoded data is not a of {LibType.PCB} type')

            return lib
        except binascii.Error:
            raise InvalidFootprintApiError(f'Invalid base64 encoded data. Incorrect padding')
        except IOError as err:
            raise InvalidFootprintApiError(f'The given Altium file is corrupt',
                                           err.args[0] if len(err.args) > 0 else None)
    else:
        raise InvalidFootprintApiError('Encoded library data not provided')


def store_footprint_data(footprint_id, encoded_data):
    footprint = FootprintReference.query.get(footprint_id)
    if footprint is None:
        __logger.debug(f'Footprint with id={footprint_id} not found')
        raise ResourceNotFoundApiError(f'Footprint with ID {footprint_id} does not exist')
    else:
        rq_helpers.launch_storage_task(StorageResourceType.FOOTPRINT, footprint_id, encoded_data)


def create_footprint(footprint_dto):
    reference_name = footprint_dto.reference
    footprint_description = footprint_dto.description

    # Parse symbol library from encoded data
    lib = __get_library(footprint_dto)

    # Verify that the body contains enough information
    if not reference_name:
        # Try to obtain the reference from the library data
        if lib.count != 1:
            raise InvalidFootprintApiError(
                f'More than one part in the given {lib.lib_type} Library. Provide a reference')
        else:
            reference_name = lib.parts[next(iter(lib.parts.keys()))].name

    # If check that the given reference exists
    if not lib.part_exists(footprint_dto.reference):
        raise InvalidFootprintApiError(
            f'The given reference {footprint_dto.reference} does not exist in the given library')

    # If no description is provided try to populate it from library data
    if not footprint_description:
        footprint_description = lib.parts[reference_name].description

    model = FootprintReference(footprint_path=footprint_dto.path, footprint_ref=reference_name,
                               description=footprint_description)

    __logger.debug(f'Creating footprint with path={footprint_dto.path} and reference={reference_name}')

    exists = db.session.query(FootprintReference.id).filter_by(footprint_path=model.footprint_path,
                                                               footprint_ref=reference_name).scalar() is not None
    if not exists:

        # Ensure that storage status at creation time is set to NOT_STORED
        model.storage_status = StorageStatus.NOT_STORED

        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Footprint created with ID {model.id}')

        # Signal background process to store the footprint
        rq_helpers.launch_storage_task(StorageResourceType.FOOTPRINT, model.id, footprint_dto.encoded_data)

        return model
    else:
        __logger.warning(
            f'Cannot create the given footprint cause already exists path={model.footprint_path} and reference={reference_name}')
        raise ResourceAlreadyExistsApiError(msg='The given footprint already exists')


def get_footprint(footprint_id):
    __logger.debug(f'Querying footprint with id={footprint_id}')
    footprint = FootprintReference.query.get(footprint_id)
    if footprint is None:
        __logger.debug(f'Footprint with id={footprint_id} not found')
        raise ResourceNotFoundApiError(f'Footprint with ID {footprint_id} does not exist')
    else:
        return footprint


def get_footprint_data_file(footprint_id):
    footprint = get_footprint(footprint_id)
    return footprint.footprint_path
