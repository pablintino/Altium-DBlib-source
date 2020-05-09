from models import ComponentModel
from sqlalchemy import inspect
from models import ModelDescriptor, FieldModelDescriptor
from sqlalchemy.orm.properties import ColumnProperty


def get_component_metadata():
    mapper = inspect(ComponentModel)
    components = {}
    for inheritance_inst in filter(
            lambda x: mapper.polymorphic_map[x].polymorphic_identity != mapper.polymorphic_identity,
            mapper.polymorphic_map):
        comp_mapper = mapper.polymorphic_map[inheritance_inst]
        model_descritor = ModelDescriptor(inheritance_inst)
        for attr in comp_mapper.attrs:
            if type(attr) is ColumnProperty:
                model_descritor.add_field(attr.key, attr.expression.unique or attr.expression.primary_key,
                                          attr.expression.nullable)
        components[inheritance_inst] = model_descritor
    return components


def get_poymorphic_component_models():
    models = {}
    mapper = inspect(ComponentModel)
    for inheritance_inst in filter(
            lambda x: mapper.polymorphic_map[x].polymorphic_identity != mapper.polymorphic_identity,
            mapper.polymorphic_map):
        comp_mapper = mapper.polymorphic_map[inheritance_inst]
        models[inheritance_inst] = comp_mapper.entity

    return models
