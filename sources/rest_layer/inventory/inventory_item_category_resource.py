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
from dtos.inventory_dtos import InventoryCategoryReferenceDto
from dtos.schemas.inventory_schemas import InventoryCategoryReferenceSchema
from rest_layer.base_api_resource import BaseApiResource
from services import inventory_service
from services.exceptions import ApiError


class InventoryItemCategoryResource(BaseApiResource):

    def post(self, id):
        try:
            category_reference_dto = InventoryCategoryReferenceSchema().load(data=request.json)
            category_id = inventory_service.set_item_category(id, category_reference_dto.category_id)
            return InventoryCategoryReferenceSchema().dump(InventoryCategoryReferenceDto.from_model(category_id)), 200
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def delete(self, id):
        try:
            inventory_service.delete_item_category(id)
            return {}, 204
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
