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

from dtos.schemas.symbol_schemas import SymbolSchema
from dtos.symbols_dtos import SymbolDto
from services import symbols_service
from services.exceptions import ResourceAlreadyExists, ResourceNotFoundError, InvalidSymbolError


class SymbolResource(Resource):
    def post(self):
        try:
            symbol_dto = SymbolSchema().load(data=request.json)
            symbol_model = symbols_service.create_symbol(symbol_dto)
            return SymbolSchema().dump(SymbolDto.from_model(symbol_model, '')), 201
        except InvalidSymbolError as error:
            return {"errors": error.msg, "details": error.details}, 400
        except ValidationError as error:
            return {"errors": error.messages}, 400
        except ResourceAlreadyExists as error:
            return {"errors": error.msg, "details": error.details}, 400

    def get(self, id):
        try:
            symbol_model = symbols_service.get_symbol(id)
            return SymbolSchema().dump(SymbolDto.from_model(symbol_model, '')), 201
        except ResourceNotFoundError as error:
            return {"errors": error.msg}, 404
