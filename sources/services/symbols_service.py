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
from models import LibraryReference
from models.internal.internal_models import StorageResourceType, StorageStatus
from services.exceptions import ResourceAlreadyExistsApiError, ResourceNotFoundApiError, InvalidSymbolApiError
from tasks import rq_helpers
from utils import parse_olefile_library, LibType

__logger = logging.getLogger(__name__)


def __get_library(symbol_dto):
    # If binary is provided try to parse it
    if symbol_dto.encoded_data:
        try:
            # Parse the given data
            decoded_data = base64.b64decode(symbol_dto.encoded_data)
            lib = parse_olefile_library(decoded_data)

            # Be sure that a Schematic library has been provided
            if lib.lib_type != LibType.SCH:
                raise InvalidSymbolApiError(f'The given encoded data is not a of {LibType.SCH} type')

            return lib
        except binascii.Error:
            raise InvalidSymbolApiError(f'Invalid base64 encoded data. Incorrect padding')
        except IOError as err:
            raise InvalidSymbolApiError(f'The given Altium file is corrupt', err.args[0] if len(err.args) > 0 else None)
    else:
        raise InvalidSymbolApiError('Encoded library data not provided')


def store_symbol_data(symbol_id, encoded_data):
    footprint = LibraryReference.query.get(symbol_id)
    if footprint is None:
        __logger.debug(f'Symbol with id={symbol_id} not found')
        raise ResourceNotFoundApiError(f'Symbol with ID {symbol_id} does not exist')
    else:
        rq_helpers.launch_storage_task(StorageResourceType.SYMBOL, symbol_id, encoded_data)


def create_symbol(symbol_dto):
    reference_name = symbol_dto.reference
    symbol_description = symbol_dto.description

    # Parse symbol library from encoded data
    lib = __get_library(symbol_dto)

    # Verify that the body contains enough information
    if not reference_name:
        # Try to obtain the reference from the library data
        if lib.count != 1:
            raise InvalidSymbolApiError(f'More than one part in the given {lib.lib_type} Library. Provide a reference')
        else:
            reference_name = lib.parts[next(iter(lib.parts.keys()))].name

    # If check that the given reference exists
    if not lib.part_exists(symbol_dto.reference):
        raise InvalidSymbolApiError(f'The given reference {symbol_dto.reference} does not exist in the given library')

    # If no description is provided try to populate it from library data
    if not symbol_description:
        symbol_description = lib.parts[reference_name].description

    model = LibraryReference(symbol_path=symbol_dto.path, symbol_ref=reference_name, description=symbol_description)

    __logger.debug(f'Creating symbol with path={symbol_dto.path} and reference={reference_name}')
    exists = db.session.query(LibraryReference.id).filter_by(symbol_path=symbol_dto.path,
                                                             symbol_ref=reference_name).scalar() is not None
    if not exists:

        # Ensure that storage status at creation time is set to NOT_STORED
        model.storage_status = StorageStatus.NOT_STORED

        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Symbol created with ID {model.id}')

        # Signal background process to store the symbol
        rq_helpers.launch_storage_task(StorageResourceType.SYMBOL, model.id, symbol_dto.encoded_data)

        return model
    else:
        __logger.warning(
            f'Cannot create the given symbol cause already exists path={symbol_dto.path} and reference={reference_name}')
        raise ResourceAlreadyExistsApiError(msg='The given symbol already exists')


def get_symbol(symbol_id):
    __logger.debug(f'Querying symbol with id={symbol_id}')
    symbol = LibraryReference.query.get(symbol_id)
    if symbol is None:
        __logger.debug(f'Symbol with id={symbol_id} not found')
        raise ResourceNotFoundApiError(f'Symbol with ID {symbol_id} does not exist')
    else:
        return symbol


def get_symbol_data_file(symbol_id):
    symbol = get_symbol(symbol_id)
    return symbol.symbol_path

