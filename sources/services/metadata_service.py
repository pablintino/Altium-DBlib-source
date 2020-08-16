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


from models.metadata import metadata_utils
import logging

from services.exceptions import InvalidComponentTypeError

__logger = logging.getLogger(__name__)

# Stores components metadata to present it to api consumers
__component_metadata = {}
__polymorphic_identities = {}
__common_component_metadata = {}


def get_components_metadata():
    items = []
    for comp_name, comp_type in __component_metadata.items():
        items.append(comp_type)
    return items


def get_component_metadata(component_type):
    global __component_metadata
    return __component_metadata.get(component_type, None)


def is_component_type_valid(component_type):
    global __component_metadata
    if component_type:
        return not __component_metadata.get(component_type, None) is None
    else:
        return False


def validate_component_fields(fields, component_type=None):
    global __common_component_metadata
    global __component_metadata

    non_recognised_fields = []

    model_metadata = __common_component_metadata
    if component_type:
        component_descriptor = __component_metadata.get(component_type, None)
        # Usually the calling function performs this check before
        if not component_descriptor:
            raise InvalidComponentTypeError('Component type ' + component_type + ' not valid')
        else:
            model_metadata = component_descriptor

    for field in fields:
        if not model_metadata.get_field(field):
            non_recognised_fields.append(field)

    return len(non_recognised_fields) == 0, non_recognised_fields


def get_polymorphic_model(model_type):
    global __polymorphic_identities
    if model_type in __polymorphic_identities:
        return __polymorphic_identities[model_type]
    return None


def __init():
    global __component_metadata
    global __polymorphic_identities
    global __common_component_metadata
    __component_metadata = metadata_utils.get_component_metadata()
    __polymorphic_identities = metadata_utils.get_polymorphic_component_models()
    __common_component_metadata = metadata_utils.get_common_component_metadata()


# Initialize service instance
__init()
