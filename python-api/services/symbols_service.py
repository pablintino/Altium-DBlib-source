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


import logging
from app import db
from dtos.symbols_dtos import SymbolDto
from models import LibraryReference
from services.exceptions import ResourceAlreadyExists, ResourceNotFoundError

__logger = logging.getLogger(__name__)


def create_symbol(symbol_dto):
    model = SymbolDto.to_model(symbol_dto)
    __logger.debug(f'Creating symbol with path={symbol_dto.path} and reference={symbol_dto.reference}')
    exists = db.session.query(LibraryReference.id).filter_by(symbol_path=symbol_dto.path,
                                                             symbol_ref=symbol_dto.reference).scalar() is not None
    if not exists:
        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Symbol created with ID {model.id}')
        return model
    else:
        __logger.warning(
            f'Cannot create the given symbol cause already exists path={symbol_dto.path} and reference={symbol_dto.reference}')
        raise ResourceAlreadyExists(msg='The given symbol already exists')


def get_symbol(symbol_id):
    __logger.debug(f'Querying symbol with id={symbol_id}')
    symbol = LibraryReference.query.get(symbol_id)
    if symbol is None:
        raise ResourceNotFoundError(f'Component with ID {symbol_id} does not exist')
    else:
        return symbol
