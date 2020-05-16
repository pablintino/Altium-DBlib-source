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
from dtos.components_dtos import CrystalOscillatorDto, DiodeRectifierDto, DiodeTVSDto, FerriteBeadDto, ResistorDto, \
    TransistorMosfetDto, CapacitorDto, DiodeZenerDto, PowerInductorDto, TransistorBjtDto, VoltageRegulatorDCDCDto, \
    VoltageRegulatorLinearDto, MicrocontrollerDto, OpAmpDto, PotentiometerDto, MemoryDto, OptocouplerDigitalDto, \
    OptocouplerLinearDto, SwitchPushButtonDto, SwitchSwitchDto, TransceiverDto, ConnectorPcbDto
from marshmallow import fields, post_load


class ComponentSchema(marshmallow.Schema):
    id = fields.Integer(missing=None, default=None)
    type = fields.String()
    mpn = fields.String(required=True)
    manufacturer = fields.String(required=True)
    value = fields.String(allow_none=True)
    package = fields.String()
    description = fields.String()
    is_through_hole = fields.Boolean()
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


class TransistorMosfetSchema(ComponentSchema):
    rds_on = fields.String()
    vgs_th = fields.String()
    vds_max = fields.String()
    ids_max = fields.String()
    power_max = fields.String()
    channel_type = fields.String()

    @post_load
    def make_transistor_mosfet_dto(self, data, **kwargs):
        return TransistorMosfetDto(**data)


class PowerInductorSchema(ComponentSchema):
    power_max = fields.String()
    tolerance = fields.String()

    @post_load
    def make_power_inductor_dto(self, data, **kwargs):
        return PowerInductorDto(**data)


class TransistorBjtSchema(ComponentSchema):
    forward_voltage = fields.String()
    reverse_current_leakage = fields.String()
    max_forward_average_current = fields.String()
    max_reverse_vrrm = fields.String()
    diode_type = fields.String()

    @post_load
    def make_transistor_bjt_dto(self, data, **kwargs):
        return TransistorBjtDto(**data)


class VoltageRegulatorDCDCSchema(ComponentSchema):
    voltage_input_min = fields.String()
    voltage_output_min_fixed = fields.String()
    voltage_output_max = fields.String()
    current_output = fields.String()
    frequency_switching = fields.String()
    topology = fields.String()
    output_type = fields.String()
    number_of_outputs = fields.String()

    @post_load
    def make_voltage_regulator_dcdc_dto(self, data, **kwargs):
        return VoltageRegulatorDCDCDto(**data)


class VoltageRegulatorLinearSchema(ComponentSchema):
    gain_bandwith = fields.String()
    output_type = fields.String()
    voltage_output_min_fixed = fields.String()
    voltage_output_max = fields.String()
    voltage_dropout_max = fields.String()
    current_supply_max = fields.String()
    current_output = fields.String()
    pssr = fields.String()

    @post_load
    def make_voltage_regulator_linear_dto(self, data, **kwargs):
        return VoltageRegulatorLinearDto(**data)


class MicrocontrollerSchema(ComponentSchema):
    core = fields.String()
    core_size = fields.String()
    speed = fields.String()
    flash_size = fields.String()
    ram_size = fields.String()
    peripherals = fields.String()
    connectivity = fields.String()
    voltage_supply = fields.String()

    @post_load
    def make_microcontroller_dto(self, data, **kwargs):
        return MicrocontrollerDto(**data)


class OpAmpSchema(ComponentSchema):
    gain_bandwith = fields.String()
    output_type = fields.String()
    input_type = fields.String()
    amplifier_type = fields.String()
    slew_rate = fields.String()
    voltage_supplies = fields.String()
    voltage_input_offset = fields.String()
    current_output = fields.String()

    @post_load
    def make_opamp_dto(self, data, **kwargs):
        return OpAmpDto(**data)


class PotentiometerSchema(ComponentSchema):
    power_max = fields.String()
    tolerance = fields.String()
    resistance_min = fields.String()
    resistance_max = fields.String()
    number_of_turns = fields.String()

    @post_load
    def make_potentiometer_dto(self, data, **kwargs):
        return PotentiometerDto(**data)


class MemorySchema(ComponentSchema):
    technology = fields.String()
    memory_type = fields.String()
    size = fields.String()
    interface = fields.String()
    clock_frequency = fields.String()

    @post_load
    def make_memory_dto(self, data, **kwargs):
        return MemoryDto(**data)


class OptocouplerDigitalSchema(ComponentSchema):
    voltage_isolation = fields.String()
    voltage_saturation_max = fields.String()
    current_transfer_ratio_max = fields.String()
    current_transfer_ratio_min = fields.String()
    voltage_forward_typical = fields.String()
    voltage_output_max = fields.String()
    number_of_channels = fields.String()

    @post_load
    def make_optocoupler_digital_dto(self, data, **kwargs):
        return OptocouplerDigitalDto(**data)


class OptocouplerLinearSchema(ComponentSchema):
    voltage_isolation = fields.String()
    transfer_gain = fields.String()
    input_forward_voltage = fields.String()
    servo_gain = fields.String()
    transfer_gain = fields.String()
    forward_gain = fields.String()
    non_linearity = fields.String()

    @post_load
    def make_optocoupler_linear_dto(self, data, **kwargs):
        return OptocouplerLinearDto(**data)


class LedIndicatorSchema(ComponentSchema):
    forward_voltage = fields.String()
    color = fields.String()
    lens_style = fields.String()
    lens_transparency = fields.String()
    dominant_wavelength = fields.String()
    test_current = fields.String()
    size = fields.String()

    @post_load
    def make_led_indicator_dto(self, data, **kwargs):
        return OptocouplerLinearDto(**data)


class SwitchPushButtonSchema(ComponentSchema):
    function = fields.String()
    dc_voltage_rating = fields.String()
    ac_voltage_rating = fields.String()
    current_rating = fields.String()
    circuit_type = fields.String()

    @post_load
    def make_switch_push_button_dto(self, data, **kwargs):
        return SwitchPushButtonDto(**data)


class SwitchSwitchSchema(ComponentSchema):
    voltage_rating = fields.String()
    current_rating = fields.String()
    number_of_positions = fields.String()
    circuit_type = fields.String()

    @post_load
    def make_switch_switch_dto(self, data, **kwargs):
        return SwitchSwitchDto(**data)


class TransceiverSchema(ComponentSchema):
    duplex = fields.String()
    data_rate = fields.String()
    protocol = fields.String()
    voltage_supply = fields.String()


    @post_load
    def make_transceiver_dto(self, data, **kwargs):
        return TransceiverDto(**data)


class ConnectorPcbSchema(ComponentSchema):
    orientation = fields.String()
    pitch = fields.String()
    voltage_rating = fields.String()
    current_rating = fields.String()
    number_of_rows = fields.String()
    number_of_contacts = fields.String()


    @post_load
    def make_connector_pcb_dto(self, data, **kwargs):
        return ConnectorPcbDto(**data)
