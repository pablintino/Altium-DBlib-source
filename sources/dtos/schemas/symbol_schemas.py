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
from marshmallow_polyfield import PolyField

from app import marshmallow
from marshmallow import fields, post_load

from dtos.symbols_dtos import SymbolDto, SymbolComponentReferenceDto
from services.exceptions import SchemaNotAvailableError


class SymbolSchema(marshmallow.Schema):
    id = fields.Integer(missing=False, default=None)
    path = fields.String()
    reference = fields.String(required=False, missing=None)
    encoded_data = fields.String(required=False, missing=None)
    description = fields.String(required=False, missing=None)

    @post_load
    def make_symbol_dto(self, data, **kwargs):
        return SymbolDto(**data)


class SymbolComponentReferenceSchema(marshmallow.Schema):
    symbol_id = fields.Integer(required=True)

    @post_load
    def make_symbol_component_reference_dto(self, data, **kwargs):
        return SymbolComponentReferenceDto(**data)


def symbol_reference_schema_serialization_disambiguation(base_object, parent_obj):
    if isinstance(base_object, SymbolDto):
        return SymbolSchema()
    elif isinstance(base_object, SymbolComponentReferenceDto):
        return SymbolComponentReferenceSchema()
    else:
        raise SchemaNotAvailableError(f'Cannot obtain a schema for the given content')


def symbol_reference_schema_deserialization_disambiguation(object_dict, parent_object_dict):
    if object_dict.get('symbol_id'):
        return SymbolComponentReferenceSchema()
    elif object_dict.get('path'):
        return SymbolSchema()
    else:
        raise SchemaNotAvailableError(f'Cannot obtain a schema for the given content')


class SymbolComponentReferenceQueryWrapperSchema(marshmallow.Schema):
    data = PolyField(
        serialization_schema_selector=symbol_reference_schema_serialization_disambiguation,
        deserialization_schema_selector=symbol_reference_schema_deserialization_disambiguation,
        default=None
    )
