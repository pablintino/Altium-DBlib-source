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


from app import marshmallow
from marshmallow import fields, post_load
from dtos.footprints_dtos import FootprintDto, FootprintComponentReferenceDto


class FootprintSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    path = fields.String()
    reference = fields.String(required=None, missing=None)
    encoded_data = fields.String(required=None, missing=None)
    description = fields.String(required=None, missing=None)

    @post_load
    def make_footprint_dto(self, data, **kwargs):
        return FootprintDto(**data)


class FootprintComponentReferenceSchema(marshmallow.Schema):
    footprint_id = fields.Integer(required=True)

    @post_load
    def make_footprint_component_reference_dto(self, data, **kwargs):
        return FootprintComponentReferenceDto(**data)
