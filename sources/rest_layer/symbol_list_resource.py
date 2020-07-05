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
from flask_restful import Resource
from marshmallow import ValidationError

from dtos.generic_objects_search_dtos import SearchPageResultDto
from dtos.schemas.generic_objects_search_schemas import SymbolsSearchPageResultSchema
from dtos.schemas.symbol_schemas import SymbolSchema
from dtos.symbols_dtos import SymbolDto
from models.internal.internal_models import StorableLibraryResourceType
from services import storable_objects_service
from services.exceptions import ApiError


class SymbolListResource(Resource):
    def post(self):
        try:
            symbol_dto = SymbolSchema().load(data=request.json)
            symbol_model = storable_objects_service.create_storable_library_object(
                                storable_type=StorableLibraryResourceType.SYMBOL,
                                reference_name=symbol_dto.reference,
                                storable_path=symbol_dto.path,
                                description=symbol_dto.description,
                                encoded_data=symbol_dto.encoded_data)
            return SymbolSchema().dump(SymbolDto.from_model(symbol_model, None)), 201
        except ApiError as error:
            return error.format_api_data()
        except ValidationError as error:
            return {"errors": error.messages}, 400

    def get(self):
        page_n = request.args.get('page_n', default=1, type=int)
        page_size = request.args.get('page_size', default=20, type=int)
        try:
            page = storable_objects_service.get_storable_objects(StorableLibraryResourceType.SYMBOL, page_n, page_size)
            dtos = []
            for object in page.items:
                dtos.append(SymbolDto.from_model(object, None))
            page_dto = SearchPageResultDto(page_size=page.per_page, page_number=page.page, total_elements=page.total,
                                           elements=dtos)
            return SymbolsSearchPageResultSchema().dump(page_dto), 200
        except ApiError as error:
            return error.format_api_data()
