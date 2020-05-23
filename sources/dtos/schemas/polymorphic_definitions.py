from dtos.schemas import schema_mapper


def shape_schema_serialization_disambiguation(base_object, parent_obj):
    schema_type = schema_mapper.get_schema_for_dto_class_name(base_object.__class__.__name__)
    if not schema_type:
        raise TypeError("Could not detect type. "
                        "Did not have a base or a length. "
                        "Are you sure this is a shape?")
    return schema_type()


def shape_schema_deserialization_disambiguation(object_dict, parent_object_dict):
    schema_type = schema_mapper.get_schema_for_component_name(object_dict.get('type'))
    if not schema_type:
        raise TypeError("Could not detect type. "
                        "Did not have a base or a length. "
                        "Are you sure this is a shape?")
    else:
        return schema_type()