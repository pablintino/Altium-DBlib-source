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


class ComponentDto:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', '')
        self.mpn = kwargs.get('mpn', '')
        self.manufacturer = kwargs.get('manufacturer', '')
        self.value = kwargs.get('value', '')
        self.package = kwargs.get('package', '')
        self.description = kwargs.get('description', '')
        self.comment = kwargs.get('comment', '')
        self.is_through_hole = kwargs.get('is_through_hole', None)

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )


class BjtTransistorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(BjtTransistorDto, self).__init__(**kwargs)
        self.vce_sat_max = kwargs.get('vce_sat_max', '')
        self.hfe = kwargs.get('hfe', '')
        self.vce_max = kwargs.get('vce_max', '')
        self.ic_max = kwargs.get('ic_max', '')
        self.power_max = kwargs.get('power_max', '')
        self.bjt_type = kwargs.get('bjt_type', '')


class CapacitorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(CapacitorDto, self).__init__(**kwargs)
        self.tolerance = kwargs.get('tolerance', '')
        self.composition = kwargs.get('composition', '')
        self.voltage = kwargs.get('voltage', '')


class CrystalOscillatorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(CrystalOscillatorDto, self).__init__(**kwargs)
        self.load_capacitance = kwargs.get('load_capacitance', '')
        self.frequency = kwargs.get('frequency', '')
        self.frequency_tolerance = kwargs.get('frequency_tolerance', '')


class DiodeRectifierDto(ComponentDto):
    def __init__(self, **kwargs):
        super(DiodeRectifierDto, self).__init__(**kwargs)
        self.forward_voltage = kwargs.get('forward_voltage', '')
        self.reverse_current_leakage = kwargs.get('reverse_current_leakage', '')
        self.max_forward_average_current = kwargs.get('max_forward_average_current', '')
        self.max_reverse_vrrm = kwargs.get('max_reverse_vrrm', '')
        self.diode_type = kwargs.get('diode_type', '')


class DiodeTVSDto(ComponentDto):
    def __init__(self, **kwargs):
        super(DiodeTVSDto, self).__init__(**kwargs)
        self.voltage_reverse_standoff = kwargs.get('voltage_reverse_standoff', '')
        self.voltage_breakdown_min = kwargs.get('voltage_breakdown_min', '')
        self.voltage_clamping_max = kwargs.get('voltage_clamping_max', '')


class DiodeZenerDto(ComponentDto):
    def __init__(self, **kwargs):
        super(DiodeZenerDto, self).__init__(**kwargs)
        self.tolerance = kwargs.get('tolerance', '')
        self.power_max = kwargs.get('power_max', '')
        self.voltage_forward = kwargs.get('voltage_forward', '')
        self.voltage_zener = kwargs.get('voltage_zener', '')


class FerriteBeadDto(ComponentDto):
    def __init__(self, **kwargs):
        super(FerriteBeadDto, self).__init__(**kwargs)
        self.number_of_lines = kwargs.get('number_of_lines', '')
        self.dc_resistance = kwargs.get('dc_resistance', '')
        self.impedance_freq = kwargs.get('impedance_freq', '')
        self.current_rating = kwargs.get('current_rating', '')


class MosfetTransistorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(MosfetTransistorDto, self).__init__(**kwargs)
        self.rds_on = kwargs.get('rds_on', '')
        self.vgs_th = kwargs.get('vgs_th', '')
        self.vds_max = kwargs.get('vds_max', '')
        self.ids_max = kwargs.get('ids_max', '')
        self.power_max = kwargs.get('power_max', '')
        self.channel_type = kwargs.get('channel_type', '')


class PowerInductorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(PowerInductorDto, self).__init__(**kwargs)
        self.resistance_dcr = kwargs.get('resistance_dcr', '')
        self.inductance_freq_test = kwargs.get('inductance_freq_test', '')
        self.current_rating = kwargs.get('current_rating', '')
        self.current_saturation = kwargs.get('current_saturation', '')
        self.core_material = kwargs.get('core_material', '')


class ResistorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(ResistorDto, self).__init__(**kwargs)
        self.power_max = kwargs.get('power_max', '')
        self.tolerance = kwargs.get('tolerance', '')


class DCDCVoltageRegulatorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(DCDCVoltageRegulatorDto, self).__init__(**kwargs)
        self.voltage_input_min = kwargs.get('voltage_input_min', '')
        self.voltage_output_min_fixed = kwargs.get('voltage_output_min_fixed', '')
        self.voltage_output_max = kwargs.get('voltage_output_max', '')
        self.current_output = kwargs.get('current_output', '')
        self.frequency_switching = kwargs.get('frequency_switching', '')
        self.topology = kwargs.get('topology', '')
        self.output_type = kwargs.get('output_type', '')
        self.number_of_outputs = kwargs.get('number_of_outputs', '')


class LinearVoltageRegulatorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(LinearVoltageRegulatorDto, self).__init__(**kwargs)
        self.gain_bandwith = kwargs.get('gain_bandwith', '')
        self.output_type = kwargs.get('output_type', '')
        self.voltage_output_min_fixed = kwargs.get('voltage_output_min_fixed', '')
        self.voltage_output_max = kwargs.get('voltage_output_max', '')
        self.voltage_dropout_max = kwargs.get('voltage_dropout_max', '')
        self.current_supply_max = kwargs.get('current_supply_max', '')
        self.current_output = kwargs.get('current_output', '')
        self.pssr = kwargs.get('pssr', '')


class MicrocontrollerDto(ComponentDto):
    def __init__(self, **kwargs):
        super(MicrocontrollerDto, self).__init__(**kwargs)
        self.core = kwargs.get('core', '')
        self.core_size = kwargs.get('core_size', '')
        self.speed = kwargs.get('speed', '')
        self.flash_size = kwargs.get('flash_size', '')
        self.ram_size = kwargs.get('ram_size', '')
        self.peripherals = kwargs.get('peripherals', '')
        self.connectivity = kwargs.get('connectivity', '')
        self.voltage_supply = kwargs.get('voltage_supply', '')


class OpAmpDto(ComponentDto):
    def __init__(self, **kwargs):
        super(OpAmpDto, self).__init__(**kwargs)
        self.gain_bandwith = kwargs.get('gain_bandwith', '')
        self.output_type = kwargs.get('output_type', '')
        self.input_type = kwargs.get('input_type', '')
        self.amplifier_type = kwargs.get('amplifier_type', '')
        self.slew_rate = kwargs.get('slew_rate', '')
        self.voltage_supplies = kwargs.get('voltage_supplies', '')
        self.voltage_input_offset = kwargs.get('voltage_input_offset', '')
        self.current_output = kwargs.get('current_output', '')


class PotentiometerDto(ComponentDto):
    def __init__(self, **kwargs):
        super(PotentiometerDto, self).__init__(**kwargs)
        self.power_max = kwargs.get('power_max', '')
        self.tolerance = kwargs.get('tolerance', '')
        self.resistance_min = kwargs.get('resistance_min', '')
        self.resistance_max = kwargs.get('resistance_max', '')
        self.number_of_turns = kwargs.get('number_of_turns', '')


class MemoryDto(ComponentDto):
    def __init__(self, **kwargs):
        super(MemoryDto, self).__init__(**kwargs)
        self.technology = kwargs.get('technology', '')
        self.memory_type = kwargs.get('memory_type', '')
        self.size = kwargs.get('size', '')
        self.interface = kwargs.get('interface', '')
        self.clock_frequency = kwargs.get('clock_frequency', '')


class OptocouplerDigitalDto(ComponentDto):
    def __init__(self, **kwargs):
        super(OptocouplerDigitalDto, self).__init__(**kwargs)
        self.voltage_isolation = kwargs.get('voltage_isolation', '')
        self.voltage_saturation_max = kwargs.get('voltage_saturation_max', '')
        self.current_transfer_ratio_max = kwargs.get('current_transfer_ratio_max', '')
        self.current_transfer_ratio_min = kwargs.get('current_transfer_ratio_min', '')
        self.voltage_forward_typical = kwargs.get('voltage_forward_typical', '')
        self.voltage_output_max = kwargs.get('voltage_output_max', '')
        self.number_of_channels = kwargs.get('number_of_channels', '')


class OptocouplerLinearDto(ComponentDto):
    def __init__(self, **kwargs):
        super(OptocouplerLinearDto, self).__init__(**kwargs)
        self.voltage_isolation = kwargs.get('voltage_isolation', '')
        self.transfer_gain = kwargs.get('transfer_gain', '')
        self.input_forward_voltage = kwargs.get('input_forward_voltage', '')
        self.servo_gain = kwargs.get('servo_gain', '')
        self.forward_gain = kwargs.get('forward_gain', '')
        self.non_linearity = kwargs.get('non_linearity', '')


class LedIndicatorDto(ComponentDto):
    def __init__(self, **kwargs):
        super(LedIndicatorDto, self).__init__(**kwargs)
        self.forward_voltage = kwargs.get('forward_voltage', '')
        self.color = kwargs.get('color', '')
        self.lens_style = kwargs.get('lens_style', '')
        self.lens_transparency = kwargs.get('lens_transparency', '')
        self.dominant_wavelength = kwargs.get('dominant_wavelength', '')
        self.test_current = kwargs.get('test_current', '')
        self.lens_size = kwargs.get('lens_size', '')


class SwitchPushButtonDto(ComponentDto):

    def __init__(self, **kwargs):
        super(SwitchPushButtonDto, self).__init__(**kwargs)
        self.function = kwargs.get('function', '')
        self.dc_voltage_rating = kwargs.get('dc_voltage_rating', '')
        self.ac_voltage_rating = kwargs.get('ac_voltage_rating', '')
        self.current_rating = kwargs.get('current_rating', '')
        self.circuit_type = kwargs.get('circuit_type', '')


class SwitchSwitchDto(ComponentDto):

    def __init__(self, **kwargs):
        super(SwitchSwitchDto, self).__init__(**kwargs)
        self.voltage_rating = kwargs.get('voltage_rating', '')
        self.current_rating = kwargs.get('current_rating', '')
        self.number_of_positions = kwargs.get('number_of_positions', '')
        self.circuit_type = kwargs.get('circuit_type', '')


class TransceiverDto(ComponentDto):

    def __init__(self, **kwargs):
        super(TransceiverDto, self).__init__(**kwargs)
        self.duplex = kwargs.get('duplex', '')
        self.data_rate = kwargs.get('data_rate', '')
        self.protocol = kwargs.get('protocol', '')
        self.voltage_supply = kwargs.get('voltage_supply', '')


class ConnectorPcbDto(ComponentDto):

    def __init__(self, **kwargs):
        super(ConnectorPcbDto, self).__init__(**kwargs)
        self.orientation = kwargs.get('orientation', '')
        self.pitch = kwargs.get('pitch', '')
        self.voltage_rating = kwargs.get('voltage_rating', '')
        self.current_rating = kwargs.get('current_rating', '')
        self.number_of_rows = kwargs.get('number_of_rows', '')
        self.number_of_contacts = kwargs.get('number_of_contacts', '')
