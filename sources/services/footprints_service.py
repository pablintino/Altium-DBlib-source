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
from dtos.footprints_dtos import FootprintDto
from dtos.symbols_dtos import SymbolDto
from models import LibraryReference, FootprintReference
from services.exceptions import ResourceAlreadyExists, ResourceNotFoundError

__logger = logging.getLogger(__name__)


def create_footprint(footprint_dto):
    model = FootprintDto.to_model(footprint_dto)
    __logger.debug(f'Creating footprint with path={footprint_dto.path} and reference={footprint_dto.reference}')
    exists = db.session.query(FootprintReference.id).filter_by(footprint_path=footprint_dto.path,
                                                               footprint_ref=footprint_dto.reference).scalar() is not None
    if not exists:
        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Footprint created with ID {model.id}')
        return model
    else:
        __logger.warning(
            f'Cannot create the given footprint cause already exists path={footprint_dto.path} and reference={footprint_dto.reference}')
        raise ResourceAlreadyExists(msg='The given footprint already exists')


def get_footprint(footprint_id):
    __logger.debug(f'Querying footprint with id={footprint_id}')
    symbol = FootprintReference.query.get(footprint_id)
    if symbol is None:
        raise ResourceNotFoundError(f'Footprint with ID {footprint_id} does not exist')
    else:
        return symbol
