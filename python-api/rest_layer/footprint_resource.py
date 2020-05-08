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
from services import footprints_service
from services.exceptions import ResourceAlreadyExists, ResourceNotFoundError


class FootprintResource(Resource):
    def post(self):
        try:
            footprint_dto = FootprintSchema().load(data=request.json)
            footprint_model = footprints_service.create_footprint(footprint_dto)
            return FootprintSchema().dump(FootprintDto.from_model(footprint_model, '')), 201
        except ValidationError as error:
            print(error.messages)
            return {"errors": error.messages}, 400
        except ResourceAlreadyExists as error:
            return {"errors": error.msg}, 400

    def get(self, id):
        try:
            footprints_model = footprints_service.get_footprint(id)
            return FootprintSchema().dump(FootprintDto.from_model(footprints_model, '')), 201
        except ResourceNotFoundError as error:
            return {"errors": error.msg}, 404
