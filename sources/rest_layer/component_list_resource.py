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

from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from dtos import components_models_dto_mappings
from dtos.components_search_dtos import SearchPageResultDto
from dtos.schemas.components_search_schemas import SearchPageResultSchema
from dtos.schemas.create_component_schema import CreateComponentSchema
from rest_layer import handle_exception
from services import component_service
from services.exceptions import ApiError


class ComponentListResource(Resource):
    def post(self):
        try:
            creation_dto = CreateComponentSchema().load(data=request.json)
            model = component_service.create_component(creation_dto['specific_dto'])
            creation_dto['specific_dto'] = components_models_dto_mappings.get_mapper_for_model(model).to_dto(model)
            return CreateComponentSchema().dump(creation_dto), 201
        except ValidationError as error:
            print(error.messages)
            return {"errors": error.messages}, 400
        except ApiError as error:
            return handle_exception(error)

    def get(self):
        page_n = request.args.get('page_n', default=1, type=int)
        page_size = request.args.get('page_size', default=20, type=int)
        filters = request.args.to_dict(flat=True)
        filters.pop('page_n', None)
        filters.pop('page_size', None)
        try:
            page = component_service.get_component_search(page_n, page_size, filters)
            dtos = []
            for model in page.items:
                dtos.append(components_models_dto_mappings.get_mapper_for_model(model).to_dto(model))
            page_dto = SearchPageResultDto(page_size=page.per_page, page_number=page.page, total_elements=page.total,
                                           elements=dtos)
            return SearchPageResultSchema().dump(page_dto), 200
        except ApiError as error:
            return handle_exception(error)
