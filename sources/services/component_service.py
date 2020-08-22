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
from dtos import component_model_mapper
from models import ComponentModel, LibraryReference, FootprintReference
from services import metadata_service
from services.exceptions import ResourceAlreadyExistsApiError, ResourceNotFoundApiError, ResourceInvalidQuery, \
    RelationAlreadyExistsError, InvalidComponentFieldsError
from utils.helpers import BraceMessage as __l

__logger = logging.getLogger(__name__)


def __validate_new_component_model(model):
    reserved_fields = ['created_on', 'updated_on', 'id']
    present_fields = list({k: v for k, v in model.__dict__.items() if v and k in reserved_fields}.keys())

    if len(present_fields) > 0:
        raise InvalidComponentFieldsError('Reserved fields were provided', reserved_fields=present_fields)


def __validate_update_component_model(raw_update_fields):
    reserved_fields = ['created_on', 'updated_on', 'id', 'mpn', 'manufacturer', 'type']

    if not raw_update_fields:
        raise InvalidComponentFieldsError('Component update data cannot be empty')

    present_fields = list({k: v for k, v in raw_update_fields.items() if v and k in reserved_fields}.keys())

    if len(present_fields) > 0:
        raise InvalidComponentFieldsError('Update reserved fields were provided', reserved_fields=present_fields)


def create_component(model):
    __logger.debug(__l('Creating component [mpn={0}, manufacturer={1}]', model.mpn, model.manufacturer))

    # Check for invalid or unexpected filled fields before storing the component
    __validate_new_component_model(model)

    exists_id = db.session.query(ComponentModel.id).filter_by(mpn=model.mpn,
                                                              manufacturer=model.manufacturer).scalar()
    if exists_id:
        raise ResourceAlreadyExistsApiError('Cannot create the requested component cause it already exists',
                                            conflicting_id=exists_id)

    db.session.add(model)
    db.session.commit()
    __logger.debug(__l('Component created [id={0}]', model.id))
    return model


def update_component(component_id, raw_update_fields):
    __logger.debug(__l('Updating component [component_id={0}]', component_id))

    component = ComponentModel.query.get(component_id)
    if not component:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)

    # Check for invalid or unexpected filled fields before storing the component
    __validate_update_component_model(raw_update_fields)

    # raw_mapped has passed field and type mapping and validation process
    raw_mapped = component_model_mapper.map_validate_raw(raw_update_fields, pk_provided=False, ignore_mandatory=True,
                                                         force_type=component.type)

    component.update_from_raw(raw_mapped)
    db.session.add(component)
    db.session.commit()
    __logger.debug(__l('Component updated [id={0}, mpn={1}, manufacturer={2}]', component.id, component.mpn,
                       component.manufacturer))
    return component


def update_create_symbol_relation(component_id, symbol_id, is_update=False):
    __logger.debug(
        __l('Creating new component-symbol relation [component_id={0}, symbol_id={1}]', component_id, symbol_id))
    component = ComponentModel.query.get(component_id)
    if component:
        library_ref = LibraryReference.query.get(symbol_id)
        if library_ref is not None:
            #  Just protect against false updates from bad POST usage
            if not is_update and component.library_ref_id:
                raise RelationAlreadyExistsError(__l(
                    'Cannot create relation. Component already has a relation [component_id={0}, library_ref_id={1}]',
                    component_id, component.library_ref_id))

            component.library_ref = library_ref
            component.library_ref_id = symbol_id
            db.session.add(component)
            db.session.commit()
            __logger.debug(f'Component symbol {"updated" if is_update else "created"}.'
                           f' Component {component_id} symbol {symbol_id}')
            return component
        else:
            raise ResourceNotFoundApiError('Symbol not found', missing_id=symbol_id)
    else:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)


def create_footprints_relation(component_id, footprint_ids):
    __logger.debug(__l('Creating new component-footprint relation [component_id={0}, footprint_ids={1}]', component_id,
                       footprint_ids))
    component = ComponentModel.query.get(component_id)
    footprint_refs = []

    # Verify that the component exists before trying anything else
    if not component:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)

    # Add only the footprints that are not already associated
    footprints_to_add = [foot_id for foot_id in footprint_ids if
                         foot_id not in [cfr.id for cfr in component.footprint_refs]]

    for footprint_id in footprints_to_add:
        footprint_ref = FootprintReference.query.get(footprint_id)
        if footprint_ref:
            footprint_refs.append(footprint_ref)
            db.session.add(footprint_ref)
        else:
            raise ResourceNotFoundApiError('Footprint not found', missing_id=footprint_id)

    component.footprint_refs.extend(footprint_refs)
    db.session.add(component)
    db.session.commit()
    __logger.debug(
        __l('Component footprints updated [component_id={0}, footprint_ids={1}', component_id, footprint_ids))
    return [ref.id for ref in component.footprint_refs]


def get_component_symbol_relation(component_id):
    __logger.debug(__l('Querying symbol relation for component [component_id={0}]', component_id))
    component = ComponentModel.query.get(component_id)
    if not component:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)

    return component.library_ref


def get_component_footprint_relations(component_id, complete_footprints=False):
    __logger.debug(__l('Querying footprint relations for component [component_id={0}]', component_id))
    component = ComponentModel.query.get(component_id)
    if component:
        result_list = []
        if complete_footprints:
            result_list = list(component.footprint_refs)
        else:
            for footprint in component.footprint_refs:
                result_list.append(footprint.id)
        return result_list
    else:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)


def get_component(component_id):
    __logger.debug(__l('Querying component data [component_id={0}]', component_id))
    component = db.session.query(ComponentModel.id, ComponentModel.type).filter_by(id=component_id).first()
    if not component:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)

    return metadata_service.get_polymorphic_model(component.type).query.get(component_id)


def get_component_search(page_number, page_size, filters=None):
    __logger.debug(
        __l('Querying components for search [page_number={0}, page_size={1}, filters={2}]', page_number, page_size,
            filters))

    # Allow passing empty filters
    filters = {} if not filters else filters

    component_type = filters.get('type', None)
    if component_type and not metadata_service.is_component_type_valid(component_type):
        raise ResourceInvalidQuery('The given component type does not exist', invalid_fields=['type'])

    if page_number < 1:
        raise ResourceInvalidQuery('Page number should be greater than 0', invalid_fields=['page_n'])

    if page_size < 1:
        raise ResourceInvalidQuery('Page size should be greater than 0', invalid_fields=['page_size'])

    res, inv_fields = metadata_service.validate_component_fields(filters, component_type)
    if not res:
        raise ResourceInvalidQuery('The given search query is invalid', invalid_fields=inv_fields)

    components_page = ComponentModel.query.filter_by(**filters) \
        .order_by(ComponentModel.id.desc()).paginate(page_number, per_page=page_size)
    return components_page


def delete_component(component_id):
    __logger.debug(__l('Deleting component [component_id={0}]', component_id))
    component = ComponentModel.query.get(component_id)
    if component:
        db.session.delete(component)
        db.session.commit()
        __logger.debug(__l('Deleted component [component_id={0}]', component_id))


def delete_component_symbol_relation(component_id):
    __logger.debug(__l('Deleting component symbol relation[component_id={0}]', component_id))
    component = ComponentModel.query.get(component_id)
    if not component:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)
    symbol_id = component.library_ref_id
    component.library_ref_id = None
    component.library_ref = None
    db.session.add(component)
    db.session.commit()
    __logger.debug(__l('Deleted component symbol relation [component_id={0}, symbol_id={1}]', component_id, symbol_id))


def delete_component_footprint_relation(component_id, footprint_id):
    __logger.debug(
        __l('Deleting component footprint relation[component_id={0}, footprint_id={1}]', component_id, footprint_id))
    component = ComponentModel.query.get(component_id)
    if not component:
        raise ResourceNotFoundApiError('Component not found', missing_id=component_id)

    component.footprint_refs = [x for x in component.footprint_refs if x.id != footprint_id]
    db.session.add(component)
    db.session.commit()
    __logger.debug(
        __l('Deleted component footprint relation [component_id={0}, footprint_id={1}]', component_id, footprint_id))
