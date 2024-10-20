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


from dtos.footprints_dtos import FootprintDto
from dtos.schemas.footprint_schemas import FootprintSchema
from models.internal.internal_models import StorableLibraryResourceType
from rest_layer.base_api_resource import BaseApiResource
from rest_layer.rest_layer_utils import is_encoded_data_request_flag
from services import storage_service, storable_objects_service
from services.exceptions import ApiError


class FootprintResource(BaseApiResource):

    def get(self, id):
        try:
            encoded_data = None
            model = storable_objects_service.get_storable_model(StorableLibraryResourceType.FOOTPRINT, id)
            if is_encoded_data_request_flag():
                encoded_data = storage_service.get_encoded_file_from_repo(model)
            return FootprintSchema().dump(FootprintDto.from_model(model, encoded_data)), 201
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
