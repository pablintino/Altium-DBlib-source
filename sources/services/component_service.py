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
from dtos import components_models_dto_mappings
from models import ComponentModel, LibraryReference, FootprintReference
from services import metadata_service
from services.exceptions import ResourceAlreadyExistsApiError, ResourceNotFoundApiError, ResourceInvalidQuery

__logger = logging.getLogger(__name__)


def create_component(dto):
    mapper = components_models_dto_mappings.get_mapper_for_dto(dto)
    model = mapper.to_model(dto)
    __logger.debug(f'Creating component with mpn={dto.mpn} and manufacturer={dto.manufacturer}')
    exists_id = db.session.query(ComponentModel.id).filter_by(mpn=dto.mpn,
                                                              manufacturer=dto.manufacturer).scalar()
    if not exists_id:
        db.session.add(model)
        db.session.commit()
        __logger.debug('Component created. {id=' + str(model.id) + '}')
        return model
    else:
        msg = 'Cannot create the requested component cause it already exists. {mpn=' + dto.mpn +\
              ', manufacturer=' + dto.manufacturer + '}'
        __logger.debug(msg)
        raise ResourceAlreadyExistsApiError(msg=msg, conflicting_id=exists_id)


def create_symbol_relation(component_id, symbol_id):
    __logger.debug(f'Creating new symbol relation for component {component_id} and symbol {symbol_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        library_ref = LibraryReference.query.get(symbol_id)
        if library_ref is not None:
            component.library_ref = library_ref
            component.library_ref_id = symbol_id
            db.session.add(component)
            db.session.commit()
            __logger.debug(f'Component symbol updated. Component {component_id} symbol {symbol_id}')
            return component
        else:
            raise ResourceNotFoundApiError(f'Symbol with ID {symbol_id} does not exist')
    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist')


def create_footprint_relation(component_id, footprint_id):
    __logger.debug(f'Creating new footprint relation for component {component_id} and footprint {footprint_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        footprint_ref = FootprintReference.query.get(footprint_id)
        if footprint_ref is not None:
            component.footprint_refs.append(footprint_ref)
            db.session.add(component)
            db.session.add(footprint_ref)
            db.session.commit()
            __logger.debug(f'Component footprints updated. Component {component_id} symbol {footprint_id}')
            return component
        else:
            raise ResourceNotFoundApiError(f'Footprint with ID {footprint_id} does not exist')
    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist')


def get_component_symbol_relation(component_id):
    __logger.debug(f'Querying symbol relation for component {component_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        return component.library_ref_id
    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist')


def get_component(component_id):
    __logger.debug(f'Querying component with id={component_id}')
    component = db.session.query(ComponentModel.id, ComponentModel.type).filter_by(id=component_id).first()
    if component is None:
        __logger.debug(f'Component with id={component_id} not found')
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist')
    else:
        return metadata_service.get_polymorphic_identity(component.type).query.get(component_id)


def get_component_search(page_number, page_size, filters):
    __logger.debug(f'Querying components with page number {page_number} and page size {page_size}')

    res, msg = metadata_service.are_fields_valid(filters)
    if not res:
        raise ResourceInvalidQuery(msg)

    components_page = ComponentModel.query.filter_by(**filters) \
        .order_by(ComponentModel.id.desc()).paginate(page_number, per_page=page_size)
    return components_page


def delete_component(component_id):
    __logger.debug(f'Deleting component with id={component_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        db.session.delete(component)
        db.session.commit()
        __logger.debug(f'Deleted component with id={component_id}')
