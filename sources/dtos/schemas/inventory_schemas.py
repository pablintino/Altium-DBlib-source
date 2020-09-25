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


from app import marshmallow
from marshmallow import fields, post_load
from dtos.inventory_dtos import InventoryItemDto, InventoryLocationDto, InventoryItemLocationRelationDto


class InventoryItemSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    mpn = fields.String(required=None, missing=None)
    manufacturer = fields.String(required=None, missing=None)
    name = fields.String(required=None, missing=None)
    description = fields.String()
    last_buy_price = fields.Float()
    dici = fields.String(missing=None, default=None)

    @post_load
    def make_inventory_item_dto(self, data, **kwargs):
        return InventoryItemDto(**data)


class InventoryLocationSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    name = fields.String(required=None, missing=None)
    description = fields.String()
    dici = fields.String(missing=None, default=None)

    @post_load
    def make_inventory_location_dto(self, data, **kwargs):
        return InventoryLocationDto(**data)


class InventoryItemLocationRelationSchema(marshmallow.Schema):
    location_ids = fields.List(fields.Integer())

    @post_load
    def make_footprint_ids_component_references_dto(self, data, **kwargs):
        return InventoryItemLocationRelationDto(**data)

