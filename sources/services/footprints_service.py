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
from services.exceptions import ResourceAlreadyExists, ResourceNotFoundError, InvalidFootprintError
from utils import parse_olefile_library, LibType

__logger = logging.getLogger(__name__)


def __try_get_library(footprint_dto):
    # If binary is provided try to parse it
    if footprint_dto.encoded_data:
        try:
            # Parse the given data
            decoded_data = base64.b64decode(footprint_dto.encoded_data)
            lib = parse_olefile_library(decoded_data)

            # Be sure that a PCB Library has been provided
            if lib.lib_type != LibType.PCB:
                raise InvalidFootprintError(f'The given encoded data is not a of {LibType.PCB} type')

            return lib
        except binascii.Error:
            raise InvalidFootprintError(f'Invalid base64 encoded data. Incorrect padding')
        except IOError as err:
            raise InvalidFootprintError(f'The given Altium file is corrupt', err.args[0] if len(err.args) > 0 else None)


def create_footprint(footprint_dto):
    reference_name = footprint_dto.reference
    footprint_description = footprint_dto.description

    # Parse symbol library from encoded data
    lib = __try_get_library(footprint_dto)

    # Verify that the body contains enough information
    if not reference_name and not lib:
        raise InvalidFootprintError('Neither reference name nor encoded data provided')
    elif lib:
        # Try to obtain the reference from the library data
        if lib.count != 1:
            raise InvalidFootprintError(f'More than one part in the given {lib.lib_type} Library. Provide a reference')
        else:
            reference_name = lib.parts[next(iter(lib.parts.keys()))].name

    # If reference name and lib are provided check that the reference exists
    if lib and footprint_dto.reference:
        if not lib.part_exists(footprint_dto.reference):
            raise InvalidFootprintError(
                f'The given reference {footprint_dto.reference} does not exist in the given library')

    # If library is provided but no description is given try to populate it from library
    if lib and not footprint_description:
        footprint_description = lib.parts[reference_name].description

    model = FootprintReference(footprint_path=footprint_dto.path, footprint_ref=reference_name,
                               description=footprint_description)

    __logger.debug(f'Creating footprint with path={footprint_dto.footprint_path} and reference={reference_name}')

    exists = db.session.query(FootprintReference.id).filter_by(footprint_path=model.footprint_path,
                                                               footprint_ref=reference_name).scalar() is not None
    if not exists:
        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Footprint created with ID {model.id}')
        return model
    else:
        __logger.warning(
            f'Cannot create the given footprint cause already exists path={model.footprint_path} and reference={reference_name}')
        raise ResourceAlreadyExists(msg='The given footprint already exists')


def get_footprint(footprint_id):
    __logger.debug(f'Querying footprint with id={footprint_id}')
    symbol = FootprintReference.query.get(footprint_id)
    if symbol is None:
        raise ResourceNotFoundError(f'Footprint with ID {footprint_id} does not exist')
    else:
        return symbol
