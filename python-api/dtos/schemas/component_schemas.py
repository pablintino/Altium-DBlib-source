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

from app.globals import ma
from dtos.component_dtos import CrystalOscillatorDto, DiodeRectifierDto, DiodeTVSDto, FerriteBeadDto, ResistorDto, \
    MosfetTransistorDto, CapacitorDto, DiodeZenerDto, PowerInductorDto, BjtTransistorDto
from marshmallow import fields, post_load


class ComponentSchema(ma.Schema):
    id = fields.Integer(missing=None, default=None)
    type = fields.String()
    mpn = fields.String()
    manufacturer = fields.String()
    value = fields.String()
    package = fields.String()
    description = fields.String()
    comment = fields.String()


class CrystalOscillatorSchema(ComponentSchema):
    load_capacitance = fields.String()
    frequency = fields.String()
    frequency_tolerance = fields.String()

    @post_load
    def make_crystal_oscillator_dto(self, data, **kwargs):
        return CrystalOscillatorDto(**data)


class DiodeRectifierSchema(ComponentSchema):
    forward_voltage = fields.String()
    reverse_current_leakage = fields.String()
    max_forward_average_current = fields.String()
    max_reverse_vrrm = fields.String()
    diode_type = fields.String()

    @post_load
    def make_diode_rectifier_dto(self, data, **kwargs):
        return DiodeRectifierDto(**data)


class DiodeTVSSchema(ComponentSchema):
    voltage_reverse_standoff = fields.String()
    voltage_breakdown_min = fields.String()
    voltage_clamping_max = fields.String()

    @post_load
    def make_diode_tvs_dto(self, data, **kwargs):
        return DiodeTVSDto(**data)


class FerriteBeadSchema(ComponentSchema):
    number_of_lines = fields.String()
    dc_resistance = fields.String()
    impedance_freq = fields.String()
    current_rating = fields.String()

    @post_load
    def make_ferrite_bead_dto(self, data, **kwargs):
        return FerriteBeadDto(**data)


class ResistorSchema(ComponentSchema):
    power_max = fields.String()
    tolerance = fields.String()

    @post_load
    def make_resistor_dto(self, data, **kwargs):
        return ResistorDto(**data)


class DiodeZenerSchema(ComponentSchema):
    tolerance = fields.String()
    power_max = fields.String()
    voltage_forward = fields.String()
    voltage_zener = fields.String()

    @post_load
    def make_diode_zener_dto(self, data, **kwargs):
        return DiodeZenerDto(**data)


class CapacitorSchema(ComponentSchema):
    voltage = fields.String()
    composition = fields.String()
    tolerance = fields.String()

    @post_load
    def make_capacitor_dto(self, data, **kwargs):
        return CapacitorDto(**data)


class MosfetTransistorSchema(ComponentSchema):
    rds_on = fields.String()
    vgs_th = fields.String()
    vds_max = fields.String()
    ids_max = fields.String()
    power_max = fields.String()
    channel_type = fields.String()

    @post_load
    def make_mosfet_transistor_dto(self, data, **kwargs):
        return MosfetTransistorDto(**data)


class PowerInductorSchema(ComponentSchema):
    power_max = fields.String()
    tolerance = fields.String()

    @post_load
    def make_power_inductor_dto(self, data, **kwargs):
        return PowerInductorDto(**data)


class BjtTransistorSchema(ComponentSchema):
    forward_voltage = fields.String()
    reverse_current_leakage = fields.String()
    max_forward_average_current = fields.String()
    max_reverse_vrrm = fields.String()
    diode_type = fields.String()

    @post_load
    def make_bjt_transistor_dto(self, data, **kwargs):
        return BjtTransistorDto(**data)
