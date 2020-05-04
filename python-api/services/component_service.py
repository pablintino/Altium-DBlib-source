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
from dtos import component_model_dto_mappings
from models import ComponentModel
from services.exceptions import ResourceAlreadyExists

__logger = logging.getLogger(__name__)


def create_component(dto, component_type):
    mapper = component_model_dto_mappings.get_mapper_for_dto(dto)
    model = mapper.to_model(dto)
    __logger.debug(f'Creating component with mpn={dto.mpn} and manufacturer={dto.manufacturer}')
    exists = db.session.query(ComponentModel.id).filter_by(mpn=dto.mpn,
                                                           manufacturer=dto.manufacturer).scalar() is not None
    if not exists:
        db.session.add(model)
        db.session.commit()
        __logger.debug(f'Component created with ID {model.id}')
        return model
    else:
        __logger.warning(
            f'Cannot create the given component cause already exists mpn={dto.mpn}, manufacturer={dto.manufacturer}')
        raise ResourceAlreadyExists(msg='The given component already exists')
