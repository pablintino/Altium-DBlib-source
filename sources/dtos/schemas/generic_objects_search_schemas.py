from marshmallow import fields
from app import marshmallow
from dtos.schemas.footprint_schemas import FootprintSchema
from dtos.schemas.symbol_schemas import SymbolSchema


class ComponentsSearchPageResultSchema(marshmallow.Schema):
    page_size = fields.Integer()
    page_number = fields.Integer()
    total_elements = fields.Integer()
    elements = fields.List(fields.Dict(keys=fields.Str()))


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
