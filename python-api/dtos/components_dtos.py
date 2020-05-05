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
        self.id = kwargs.get('id', '')
        self.type = kwargs.get('type', '')
        self.mpn = kwargs.get('mpn', '')
        self.manufacturer = kwargs.get('manufacturer', '')
        self.value = kwargs.get('value', '')
        self.package = kwargs.get('package', '')
        self.description = kwargs.get('description', '')
        self.comment = kwargs.get('comment', '')

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
