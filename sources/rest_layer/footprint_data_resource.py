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


import base64

from flask import send_file, request
from models.internal.internal_models import StorableLibraryResourceType
from rest_layer.base_api_resource import BaseApiResource
from services import storage_service, storable_objects_service
from services.exceptions import ApiError, InvalidMultipartFileDataError


class FootprintDataResource(BaseApiResource):
    def post(self, id):
        try:
            # Verify that the uploaded file is provided using 'data' as name
            if 'data' not in request.files:
                raise InvalidMultipartFileDataError(msg="'data' multipart element not found in request")

            with request.files['data'].stream as file:
                encoded_data = base64.b64encode(file.read())
                storable_objects_service.update_object_data(StorableLibraryResourceType.FOOTPRINT, id, encoded_data)
            return '', 204
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def get(self, id):
        try:
            model = storable_objects_service.get_storable_model(StorableLibraryResourceType.FOOTPRINT, id)
            footprint_file = storage_service.get_file_from_repo(model)
            return send_file(footprint_file, as_attachment=True)
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
