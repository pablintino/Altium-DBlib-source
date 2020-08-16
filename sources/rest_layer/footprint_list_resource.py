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

from dtos.footprints_dtos import FootprintDto
from dtos.generic_objects_search_dtos import SearchPageResultDto
from dtos.schemas.footprint_schemas import FootprintSchema
from dtos.schemas.generic_objects_search_schemas import FootprintsSearchPageResultSchema
from models.internal.internal_models import StorableLibraryResourceType
from rest_layer.base_api_resource import BaseApiResource
from services import storable_objects_service
from services.exceptions import ApiError


class FootprintListResource(BaseApiResource):
    def post(self):
        try:
            footprint_dto = FootprintSchema().load(data=request.json)
            footprint_model = storable_objects_service.create_storable_library_object(
                storable_type=StorableLibraryResourceType.FOOTPRINT,
                reference_name=footprint_dto.reference,
                storable_path=footprint_dto.path,
                description=footprint_dto.description,
                encoded_data=footprint_dto.encoded_data)
            return FootprintSchema().dump(FootprintDto.from_model(footprint_model, None)), 201
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def get(self):
        page_n = request.args.get('page_n', default=1, type=int)
        page_size = request.args.get('page_size', default=20, type=int)

        try:
            page = storable_objects_service.get_storable_objects(StorableLibraryResourceType.FOOTPRINT,
                                                                 page_n,
                                                                 page_size)
            dtos = [FootprintDto.from_model(obj, None) for obj in page.items]
            page_dto = SearchPageResultDto(page_size=page.per_page, page_number=page.page, total_elements=page.total,
                                           elements=dtos)
            return FootprintsSearchPageResultSchema().dump(page_dto), 200
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
