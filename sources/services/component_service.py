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
from models import ComponentModel, LibraryReference, FootprintReference
from services import metadata_service
from services.exceptions import ResourceAlreadyExistsApiError, ResourceNotFoundApiError, ResourceInvalidQuery, \
    RelationAlreadyExistsError, InvalidComponentFieldsError

__logger = logging.getLogger(__name__)


def __validate_new_component_model(model):
    reserved_fields = ['created_on', 'updated_on', 'id']
    present_fields = list({k: v for k, v in model.__dict__.items() if v and k in reserved_fields}.keys())

    if len(present_fields) > 0:
        raise InvalidComponentFieldsError('Reserved fields were provided', reserved_fields=present_fields)


def create_component(model):
    __logger.debug(f'Creating component with mpn={model.mpn} and manufacturer={model.manufacturer}')

    # Check for invalid or unexpected filled fields before storing the component
    __validate_new_component_model(model)

    exists_id = db.session.query(ComponentModel.id).filter_by(mpn=model.mpn,
                                                              manufacturer=model.manufacturer).scalar()
    if not exists_id:
        db.session.add(model)
        db.session.commit()
        __logger.debug('Component created. {id=' + str(model.id) + '}')
        return model
    else:
        msg = 'Cannot create the requested component cause it already exists. {mpn=' + model.mpn + \
              ', manufacturer=' + model.manufacturer + '}'
        __logger.debug(msg)
        raise ResourceAlreadyExistsApiError(msg=msg, conflicting_id=exists_id)


def update_create_symbol_relation(component_id, symbol_id, is_update=False):
    __logger.debug(f'Creating new symbol relation for component {component_id} and symbol {symbol_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        library_ref = LibraryReference.query.get(symbol_id)
        if library_ref is not None:
            #  Just protect against false updates from bad POST usage
            if not is_update and component.library_ref_id:
                msg = f'Cannot create relation cause component {component_id} has already a relation. Current ' \
                      f'symbol {str(component.library_ref_id)} '
                raise RelationAlreadyExistsError(msg)

            component.library_ref = library_ref
            component.library_ref_id = symbol_id
            db.session.add(component)
            db.session.commit()
            __logger.debug(f'Component symbol {"updated" if is_update else "created"}.'
                           f' Component {component_id} symbol {symbol_id}')
            return component
        else:
            raise ResourceNotFoundApiError(f'Symbol with ID {symbol_id} does not exist', missing_id=symbol_id)
    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist', missing_id=component_id)


def create_footprints_relation(component_id, footprint_ids):
    __logger.debug(f'Creating new footprint relation for component {component_id} and footprint {str(footprint_ids)}')
    component = ComponentModel.query.get(component_id)
    footprint_refs = []
    if component is not None:

        for footprint_id in footprint_ids:
            footprint_ref = FootprintReference.query.get(footprint_id)
            if footprint_ref:
                exists = False
                for actual_ref in component.footprint_refs:
                    if actual_ref.id == footprint_id:
                        exists = True
                        break
                if not exists:
                    footprint_refs.append(footprint_ref)
                    db.session.add(footprint_ref)
            else:
                raise ResourceNotFoundApiError(f'Footprint with ID {footprint_id} does not exist',
                                               missing_id=footprint_id)

        component.footprint_refs.extend(footprint_refs)
        db.session.add(component)
        db.session.commit()
        __logger.debug(f'Component footprints updated. Component {component_id} footprints {str(footprint_ids)}')
        return [ref.id for ref in component.footprint_refs]

    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist', missing_id=component_id)


def get_component_symbol_relation(component_id):
    __logger.debug(f'Querying symbol relation for component {component_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        return component.library_ref
    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist', missing_id=component_id)


def get_component_footprint_relations(component_id, complete_footprints=False):
    __logger.debug(f'Querying footprint relations for component {component_id}')
    component = ComponentModel.query.get(component_id)
    if component is not None:
        result_list = []
        if complete_footprints:
            result_list = list(component.footprint_refs)
        else:
            for footprint in component.footprint_refs:
                result_list.append(footprint.id)
        return result_list
    else:
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist', missing_id=component_id)


def get_component(component_id):
    __logger.debug(f'Querying component with id={component_id}')
    component = db.session.query(ComponentModel.id, ComponentModel.type).filter_by(id=component_id).first()
    if component is None:
        __logger.debug(f'Component with id={component_id} not found')
        raise ResourceNotFoundApiError(f'Component with ID {component_id} does not exist', missing_id=component_id)
    else:
        return metadata_service.get_polymorphic_model(component.type).query.get(component_id)


def get_component_search(page_number, page_size, filters):
    __logger.debug(f'Querying components with page number {page_number} and page size {page_size}')

    component_type = filters.get('type', None)
    if component_type:
        if not metadata_service.is_component_type_valid(component_type):
            raise ResourceInvalidQuery('The given component type does not exist')

    res, inv_fields = metadata_service.validate_component_fields(filters, component_type)
    if not res:
        raise ResourceInvalidQuery('The given search query is invalid', inv_fields)

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
