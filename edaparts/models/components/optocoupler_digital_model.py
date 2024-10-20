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


from sqlalchemy import Column, String, ForeignKey
from models.components.component_model import ComponentModel


class OptocouplerDigitalModel(ComponentModel):
    __tablename__ = 'optocoupler_digital'
    __id_prefix__ = 'OPTD'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a digital optocoupler
    voltage_isolation = Column(String(30))
    voltage_saturation_max = Column(String(30))
    current_transfer_ratio_max = Column(String(30))
    current_transfer_ratio_min = Column(String(30))
    voltage_forward_typical = Column(String(30))
    voltage_output_max = Column(String(30))
    number_of_channels = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
