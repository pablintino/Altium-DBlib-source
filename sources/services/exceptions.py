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


# base app exception
class ApiError(Exception):
    def __init__(self, msg=None, details=None, http_code=500):
        super(ApiError, self).__init__(msg)
        self.msg = msg
        self.details = details
        self.http_code = http_code


class ResourceNotFoundApiError(ApiError):

    def __init__(self, msg=None, details=None):
        super(ResourceNotFoundApiError, self).__init__(msg, details, 404)

    pass


class ResourceAlreadyExistsApiError(ApiError):
    def __init__(self, msg=None, details=None):
        super(ResourceAlreadyExistsApiError, self).__init__(msg, details, 400)


class ResourceInvalidQuery(ApiError):
    def __init__(self, msg=None, details=None):
        super(ResourceInvalidQuery, self).__init__(msg, details, 400)


class InvalidSymbolApiError(ApiError):
    def __init__(self, msg=None, details=None):
        super(InvalidSymbolApiError, self).__init__(msg, details, 400)


class InvalidFootprintApiError(ApiError):
    def __init__(self, msg=None, details=None):
        super(InvalidFootprintApiError, self).__init__(msg, details, 400)


class InvalidMultipartFileDataError(ApiError):
    def __init__(self, msg=None, details=None):
        super(InvalidMultipartFileDataError, self).__init__(msg, details, 400)
