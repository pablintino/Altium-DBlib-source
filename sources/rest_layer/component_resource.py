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
from dtos.components_dtos import GenericComponentDto
from dtos.schemas.component_schemas import GenericComponentSchema
from rest_layer.base_api_resource import BaseApiResource
from services import component_service
from services.exceptions import ApiError


class ComponentResource(BaseApiResource):

    def get(self, id):
        try:
            model = component_service.get_component(id)
            raw_component = component_model_mapper.map_model_to_raw(model)
            return GenericComponentSchema().dump(GenericComponentDto(raw_component)), 200
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def put(self, id):
        try:
            generic_dto_data = GenericComponentSchema().load(data=request.json)
            model = component_service.update_component(id, generic_dto_data.data)
            raw_updated_component = component_model_mapper.map_model_to_raw(model)
            return GenericComponentSchema().dump(GenericComponentDto(raw_updated_component)), 200
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()

    def delete(self, id):
        try:
            component_service.delete_component(id)
            return {}, 204
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ApiError as error:
            self.logger().debug(error)
            return error.format_api_data()
