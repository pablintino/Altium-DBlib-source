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
from flask import request
from marshmallow import ValidationError
from dtos.inventory_dtos import InventoryItemLocationStockDto
from dtos.schemas.inventory_schemas import InventoryItemLocationStockSchema
from rest_layer.base_api_resource import BaseApiResource
from services import inventory_service
from services.exceptions import ApiError


class InventoryItemStockLocationResource(BaseApiResource):

    def get(self, id, id_loc):
        try:

            item_stock = inventory_service.get_item_stock_for_location(id, id_loc)
            return InventoryItemLocationStockSchema().dump(
                InventoryItemLocationStockDto.from_model(item_stock)), 200
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def put(self, id, id_loc):
        try:
            stock_dto = InventoryItemLocationStockSchema().load(data=request.json)
            item_stock = inventory_service.update_item_location_stock_levels(id, id_loc,
                                                                             min_stock_level=stock_dto.stock_min_level,
                                                                             min_notify_level=stock_dto.stock_notify_min_level)
            return InventoryItemLocationStockSchema().dump(
                InventoryItemLocationStockDto.from_model(item_stock)), 200
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
