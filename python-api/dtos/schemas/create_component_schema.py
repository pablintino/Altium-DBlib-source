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


from marshmallow import fields
from marshmallow_polyfield import PolyField
from app import marshmallow
from dtos.schemas import schema_mapper


def shape_schema_serialization_disambiguation(base_object, parent_obj):
    schema_type = schema_mapper.get_schema_for_dto_class_name(base_object.__class__.__name__)
    if not schema_type:
        raise TypeError("Could not detect type. "
                        "Did not have a base or a length. "
                        "Are you sure this is a shape?")
    return schema_type()


def shape_schema_deserialization_disambiguation(object_dict, parent_object_dict):
    schema_type = schema_mapper.get_schema_for_dto_name(parent_object_dict.get("component_type"))
    if not schema_type:
        raise TypeError("Could not detect type. "
                        "Did not have a base or a length. "
                        "Are you sure this is a shape?")
    else:
        return schema_type()


class CreateComponentSchema(marshmallow.Schema):
    component_type = fields.String(required=True)
    specific_dto = PolyField(
        serialization_schema_selector=shape_schema_serialization_disambiguation,
        deserialization_schema_selector=shape_schema_deserialization_disambiguation,
        required=True
    )
