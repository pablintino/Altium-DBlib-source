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

import logging
from app import db

from models import ResistorModel

__logger = logging.getLogger(__name__)


def create_resistor_component(resistor_dto):
    resistor_model = ResistorModel(
        power_max=resistor_dto.power_max,
        tolerance=resistor_dto.tolerance,
        value=resistor_dto.value,
        package=resistor_dto.package,
        description=resistor_dto.description,
        comment=resistor_dto.comment,
        type=resistor_dto.type,
        mpn=resistor_dto.mpn,
        manufacturer=resistor_dto.manufacturer
    )
    return resistor_model


def create_component(dto, component_type):
    model = create_resistor_component(dto)
    db.session.add(model)
    db.session.commit()
    print(model)
