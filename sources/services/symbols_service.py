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
from services.exceptions import ResourceAlreadyExists, ResourceNotFoundError, InvalidSymbolError
from utils import parse_olefile_library, LibType

__logger = logging.getLogger(__name__)


def __try_get_library(symbol_dto):
    # If binary is provided try to parse it
    if symbol_dto.encoded_data:
        try:
            # Parse the given data
            decoded_data = base64.b64decode(symbol_dto.encoded_data)
            lib = parse_olefile_library(decoded_data)

            # Be sure that a Schematic library has been provided
            if lib.lib_type != LibType.SCH:
                raise InvalidSymbolError(f'The given encoded data is not a of {LibType.SCH} type')

            return lib
        except binascii.Error:
            raise InvalidSymbolError(f'Invalid base64 encoded data. Incorrect padding')
        except IOError as err:
            raise InvalidSymbolError(f'The given Altium file is corrupt', err.args[0] if len(err.args) > 0 else None)


def create_symbol(symbol_dto):
    reference_name = symbol_dto.reference
    symbol_description = symbol_dto.description

    # Parse symbol library from encoded data
    lib = __try_get_library(symbol_dto)

    # Verify that the body contains enough information
    if not reference_name and not lib:
        raise InvalidSymbolError('Neither reference name nor encoded data provided')
    elif lib:
        # Try to obtain the reference from the library data
        if lib.count != 1:
            raise InvalidSymbolError(f'More than one part in the given {lib.lib_type} Library. Provide a reference')
        else:
            reference_name = lib.parts[next(iter(lib.parts.keys()))].name

    # If reference name and lib are provided check that the reference exists
    if lib and symbol_dto.reference:
        if not lib.part_exists(symbol_dto.reference):
            raise InvalidSymbolError(f'The given reference {symbol_dto.reference} does not exist in the given library')

    # If library is provided but no description is given try to populate it from library
    if lib and not symbol_description:
        symbol_description = lib.parts[reference_name].description

    model = LibraryReference(symbol_path=symbol_dto.path, symbol_ref=reference_name, description=symbol_description)

    __logger.debug(f'Creating symbol with path={symbol_dto.path} and reference={reference_name}')
    exists = db.session.query(LibraryReference.id).filter_by(symbol_path=symbol_dto.path,
                                                             symbol_ref=reference_name).scalar() is not None
    if not exists:
        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Symbol created with ID {model.id}')
        return model
    else:
        __logger.warning(
            f'Cannot create the given symbol cause already exists path={symbol_dto.path} and reference={reference_name}')
        raise ResourceAlreadyExists(msg='The given symbol already exists')


def get_symbol(symbol_id):
    __logger.debug(f'Querying symbol with id={symbol_id}')
    symbol = LibraryReference.query.get(symbol_id)
    if symbol is None:
        raise ResourceNotFoundError(f'Symbol with ID {symbol_id} does not exist')
    else:
        return symbol
