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

from dtos import component_model_mapper
from dtos.generic_objects_search_dtos import SearchPageResultDto
from dtos.inventory_dtos import InventoryItemDto
from dtos.schemas.generic_objects_search_schemas import InventorySearchPageResultSchema
from dtos.schemas.inventory_schemas import InventoryItemSchema
from rest_layer import rest_layer_utils
from rest_layer.base_api_resource import BaseApiResource
from services import search_service, inventory_service
from services.exceptions import ApiError


class InventoryItemListResource(BaseApiResource):

    def post(self):
        try:
            try:
                item_dto = InventoryItemSchema().load(data=request.json)
                item_model = inventory_service.create_standalone_item(InventoryItemDto.to_model(item_dto))
                return InventoryItemSchema().dump(InventoryItemDto.from_model(item_model)), 201
            except ValidationError as error:
                return {"errors": error.messages}, 400
            except ApiError as error:
                self.logger().debug(error)
                return error.format_api_data()
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def get(self):
        try:
            page_n = request.args.get('page_n', default=1, type=int)
            page_size = request.args.get('page_size', default=20, type=int)
            include_component = rest_layer_utils.is_include_component_request_flag(True)
            filters = request.args.to_dict(flat=True)
            filters.pop('page_n', None)
            filters.pop('page_size', None)
            page = search_service.search_items(filters, page_n, page_size)
            dtos = [InventoryItemDto.from_model(item_model, component_dto=component_model_mapper.map_model_to_raw(
                item_model.component) if include_component else None) for item_model in page.items]
            page_dto = SearchPageResultDto(page_size=page.per_page, page_number=page.page, total_elements=page.total,
                                           elements=dtos)
            return InventorySearchPageResultSchema().dump(page_dto), 200
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
