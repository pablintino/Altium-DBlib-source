from marshmallow import fields
from marshmallow_polyfield import PolyField

from app import marshmallow
from dtos.schemas.footprint_schemas import FootprintSchema
from dtos.schemas.polymorphic_definitions import shape_schema_deserialization_disambiguation, \
    shape_schema_serialization_disambiguation
from dtos.schemas.symbol_schemas import SymbolSchema


class ComponentsSearchPageResultSchema(marshmallow.Schema):
    page_size = fields.Integer()
    page_number = fields.Integer()
    total_elements = fields.Integer()
    elements = PolyField(
        serialization_schema_selector=shape_schema_serialization_disambiguation,
        deserialization_schema_selector=shape_schema_deserialization_disambiguation,
        many=True
    )


class SymbolsSearchPageResultSchema(marshmallow.Schema):
    page_size = fields.Integer()
    page_number = fields.Integer()
    total_elements = fields.Integer()
    elements = fields.List(fields.Nested(SymbolSchema))


class FootprintsSearchPageResultSchema(marshmallow.Schema):
    page_size = fields.Integer()
    page_number = fields.Integer()
    total_elements = fields.Integer()
    elements = fields.List(fields.Nested(FootprintSchema))
