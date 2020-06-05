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

from flask_restful import Resource, abort
from flask import send_from_directory
from flask import request

from app import Config
from rest_layer import handle_exception
from services import symbols_service
from services.exceptions import ApiError, InvalidMultipartFileDataError


class SymbolDataResource(Resource):
    def post(self, id):
        try:
            # Verify that the uploaded file is provided using 'data' as name
            if 'data' not in request.files:
                raise InvalidMultipartFileDataError(msg="'data' multipart element not found in request")

            with request.files['data'].stream as file:
                encoded_data = base64.b64encode(file.read())
                symbols_service.store_symbol_data(id, encoded_data)
            return {}, 201
        except ApiError as error:
            return handle_exception(error)

    def get(self, id):
        try:
            file = symbols_service.get_symbol_data_file(id)
            return send_from_directory(Config.REPO_PATH, file, as_attachment=True)
        except FileNotFoundError:
            abort(404)
        except ApiError as error:
            return handle_exception(error)
