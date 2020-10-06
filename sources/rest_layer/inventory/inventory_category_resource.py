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

from dtos.inventory_dtos import InventoryCategoryDto
from dtos.schemas.inventory_schemas import InventoryCategorySchema
from rest_layer.base_api_resource import BaseApiResource
from services import inventory_service
from services.exceptions import ApiError


class InventoryCategoryResource(BaseApiResource):

    def get(self, id):
        try:
            category_model = inventory_service.get_category(id)
            return InventoryCategorySchema().dump(InventoryCategoryDto.from_model(category_model)), 201
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def put(self, id):
        try:
            category_dto = InventoryCategorySchema().load(data=request.json)
            category_model = inventory_service.update_category(id, category_dto.name, category_dto.description)
            return InventoryCategorySchema().dump(InventoryCategoryDto.from_model(category_model)), 201
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()



