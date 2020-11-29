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

from dtos import component_model_mapper
from dtos.inventory_dtos import InventoryItemDto
from dtos.schemas.inventory_schemas import InventoryItemSchema
from rest_layer import rest_layer_utils
from rest_layer.base_api_resource import BaseApiResource
from services import inventory_service
from services.exceptions import ApiError


class InventoryItemResource(BaseApiResource):

    def get(self, id):
        try:
            include_component = rest_layer_utils.is_include_component_request_flag(False)
            component_dto = None
            item_model = inventory_service.get_item(id)
            if include_component:
                component_dto = component_model_mapper.map_model_to_raw(inventory_service.get_item_component(id))
            return InventoryItemSchema().dump(InventoryItemDto.from_model(item_model, component_dto=component_dto)), 200
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def delete(self, id):
        try:
            inventory_service.delete_item(id)
            return {}, 204
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
