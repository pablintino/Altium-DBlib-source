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

from dtos.schemas.symbol_schemas import SymbolComponentReferenceSchema, SymbolSchema, \
    SymbolComponentReferenceQueryWrapperSchema
from dtos.symbols_dtos import SymbolComponentReferenceDto, SymbolDto, SymbolComponentReferenceWrapperDto
from rest_layer import rest_layer_utils
from services import component_service, storage_service
from services.exceptions import ApiError, InvalidRequestError


class SymbolComponentReferenceResource(Resource):

    def __create_update_symbol(self, id, is_update):
        try:
            reference_dto = SymbolComponentReferenceSchema().load(data=request.json)
            component_service.update_create_symbol_relation(id, reference_dto.symbol_id, is_update)
            return SymbolComponentReferenceSchema().dump(reference_dto), 200
        except ValidationError as error:
            print(error.messages)
            return {"errors": error.messages}, 400
        except ApiError as error:
            return error.format_api_data()

    def post(self, id):
        return self.__create_update_symbol(id, False)

    def put(self, id):
        return self.__create_update_symbol(id, True)

    def get(self, id):
        try:
            retrieve_all = rest_layer_utils.parse_request_all_data_flag()
            retrieve_encoded_data = rest_layer_utils.parse_request_encoded_data_flag()

            # Protection against full requests requested as an "id only" request
            if retrieve_encoded_data and not retrieve_all:
                raise InvalidRequestError('Cannot retrieve encoded metadata for a non full request')

            symbol_data = component_service.get_component_symbol_relation(id)

            if not symbol_data:
                # Empty relation. Return an empty wrapper
                resp_data = None
            elif not retrieve_all:
                resp_data = SymbolComponentReferenceDto(symbol_id=symbol_data.id)
            else:
                encoded_data = storage_service.get_encoded_file_from_repo(
                    symbol_data) if retrieve_encoded_data else None
                resp_data = SymbolDto.from_model(symbol_data, encoded_data)

            return SymbolComponentReferenceQueryWrapperSchema().dump(SymbolComponentReferenceWrapperDto(resp_data)), 200
        except ApiError as error:
            return error.format_api_data()
