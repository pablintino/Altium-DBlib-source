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
from dtos.inventory_dtos import InventoryItemDto, InventoryLocationDto, InventoryItemLocationRelationDto, \
    InventoryItemLocationStockDto, InventorySingleStockMovementDto, InventoryMassStockMovementDto, \
    InventoryItemStockStatusDto, InventoryMassStockMovementResultDto, InventoryItemPropertyDto, \
    InventoryItemPropertyUpdateDto, InventoryCategoryDto, InventoryCategoryReferenceDto


class InventoryItemSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    mpn = fields.String(required=True)
    manufacturer = fields.String(required=True)
    name = fields.String(required=True)
    description = fields.String()
    last_buy_price = fields.Float()
    dici = fields.String(missing=None, default=None)
    component = fields.Dict(keys=fields.Str(), missing=None, default=None)

    @post_load
    def make_inventory_item_dto(self, data, **kwargs):
        return InventoryItemDto(**data)


class InventoryLocationSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    name = fields.String(required=True)
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


class InventoryItemLocationStockSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    actual_stock = fields.Float()
    stock_min_level = fields.Float(missing=None, default=None)
    stock_notify_min_level = fields.Float(missing=None, default=None)


    @post_load
    def make_inventory_item_location_stock_dto(self, data, **kwargs):
        return InventoryItemLocationStockDto(**data)


class InventorySingleStockMovementSchema(marshmallow.Schema):
    item_dici = fields.String(missing=None, default=None)
    item_id = fields.Integer(missing=None, default=None)
    location_dici = fields.String(missing=None, default=None)
    location_id = fields.Integer(missing=None, default=None)
    quantity = fields.Float()

    @post_load
    def make_inventory_single_stock_movement_dto(self, data, **kwargs):
        return InventorySingleStockMovementDto(**data)


class InventoryMassStockMovementSchema(marshmallow.Schema):

    reason = fields.String()
    comment = fields.String()
    movements = fields.Nested(InventorySingleStockMovementSchema, many=True)

    @post_load
    def make_inventory_mass_stock_movement_dto(self, data, **kwargs):
        return InventoryMassStockMovementDto(**data)


class InventoryItemStockStatusSchema(marshmallow.Schema):
    stock_level = fields.Float()
    item_dici = fields.String()
    location_dici = fields.String()

    @post_load
    def make_inventory_item_stock_status_dto(self, data, **kwargs):
        return InventoryItemStockStatusDto(**data)


class InventoryMassStockMovementResultSchema(marshmallow.Schema):

    stock_levels = fields.Nested(InventoryItemStockStatusSchema, many=True)

    @post_load
    def make_inventory_mass_stock_movement_result_dto(self, data, **kwargs):
        return InventoryMassStockMovementResultDto(**data)


class InventoryItemPropertyUpdateSchema(marshmallow.Schema):
    value = fields.Raw(default=None)

    @post_load
    def make_inventory_item_property_update_dto(self, data, **kwargs):
        return InventoryItemPropertyUpdateDto(**data)


class InventoryItemPropertySchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    name = fields.String()
    value = fields.Raw(missing=None, default=None)

    @post_load
    def make_inventory_item_property_dto(self, data, **kwargs):
        return InventoryItemPropertyDto(**data)


class InventoryItemPropertiesSchema(marshmallow.Schema):
    properties = fields.Nested(InventoryItemPropertySchema, many=True)


class InventoryCategorySchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    name = fields.String(required=True)
    description = fields.String()
    parent_id = fields.Integer(missing=None, default=None)

    @post_load
    def make_inventory_category_dto(self, data, **kwargs):
        return InventoryCategoryDto(**data)


class InventoryCategoryReferenceSchema(marshmallow.Schema):
    category_id = fields.Integer(missing=None, default=None)

    @post_load
    def make_symbol_inventory_category_reference_dto(self, data, **kwargs):
        return InventoryCategoryReferenceDto(**data)

