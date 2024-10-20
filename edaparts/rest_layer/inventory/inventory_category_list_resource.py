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

from dtos.generic_objects_search_dtos import SearchPageResultDto
from dtos.inventory_dtos import InventoryCategoryDto
from dtos.schemas.generic_objects_search_schemas import InventoryCategoriesPageSchema
from dtos.schemas.inventory_schemas import InventoryCategorySchema
from rest_layer.base_api_resource import BaseApiResource
from services import inventory_service
from services.exceptions import ApiError


class InventoryCategoryListResource(BaseApiResource):

    def post(self):
        try:
            category_dto = InventoryCategorySchema().load(data=request.json)
            category_model = inventory_service.create_category(category_dto.name, category_dto.description)
            return InventoryCategorySchema().dump(InventoryCategoryDto.from_model(category_model)), 201
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def get(self):
        try:
            page_n = request.args.get('page_n', default=1, type=int)
            page_size = request.args.get('page_size', default=20, type=int)
            only_root = request.args.get('only_root', default=False, type=bool)
            page = inventory_service.get_categories(page_n, page_size, only_root)
            page_dto = SearchPageResultDto(page_size=page.per_page, page_number=page.page, total_elements=page.total,
                                           elements=[InventoryCategoryDto.from_model(model) for model in page.items])
            return InventoryCategoriesPageSchema().dump(page_dto), 200
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

