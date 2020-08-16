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

from dtos.footprints_dtos import FootprintDto
from dtos.schemas.footprint_schemas import FootprintSchema
from models.internal.internal_models import StorableLibraryResourceType
from services import storage_service, storable_objects_service
from services.exceptions import ApiError


class FootprintResource(Resource):
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
            return error.format_api_data()

    def get(self, id):
        try:
            encoded_data = None
            model = storable_objects_service.get_storable_model(StorableLibraryResourceType.FOOTPRINT, id)
            if request.args.get('encoded_data', default=False, type=bool):
                encoded_data = storage_service.get_encoded_file_from_repo(model)
            return FootprintSchema().dump(FootprintDto.from_model(model, encoded_data)), 201
        except ApiError as error:
            return error.format_api_data()
