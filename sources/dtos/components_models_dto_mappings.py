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


from abc import abstractmethod, ABC

from dtos.components_dtos import ResistorDto, CapacitorDto, CrystalOscillatorDto, DiodeRectifierDto, DiodeTVSDto, \
    DiodeZenerDto, FerriteBeadDto, TransistorMosfetDto, TransistorBjtDto, PowerInductorDto, VoltageRegulatorDCDCDto, \
    VoltageRegulatorLinearDto, MicrocontrollerDto, OpAmpDto, PotentiometerDto, MemoryDto, OptocouplerDigitalDto, \
    OptocouplerLinearDto, LedIndicatorDto, SwitchPushButtonDto, SwitchSwitchDto, TransceiverDto, ConnectorPcbDto
from models import ResistorModel, CapacitorModel, CrystalOscillatorModel, DiodeRectifierModel, DiodeZenerModel, \
    DiodeTVSModel, FerriteBeadModel, TransistorMosfetModel, TransistorBjtModel, PowerInductorModel, \
    VoltageRegulatorDCDCModel, VoltageRegulatorLinearModel, MicrocontrollerModel, OpAmpModel, PotentiometerModel, \
    MemoryModel, OptocouplerDigitalModel, OptocouplerLinearModel, SwitchPushButtonModel, SwitchSwitchModel, \
    TransceiverModel, ConnectorPcbModel, LedIndicatorModel


class DtoModelMaper(ABC):

    def __init__(self, model_type, dto_type):
        self.model_id = model_type.__name__
        self.dto_type = dto_type

    def to_dto(self, model):
        return self.dto_type(**model.__dict__)

    @abstractmethod
    def to_model(self, dto):
        pass


class ResistorModelMapper(DtoModelMaper):

    def __init__(self):
        super(ResistorModelMapper, self).__init__(ResistorModel, ResistorDto)

    def to_model(self, dto):
        return ResistorModel(
            power_max=dto.power_max,
            tolerance=dto.tolerance,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class CapactitorModelMapper(DtoModelMaper):

    def __init__(self):
        super(CapactitorModelMapper, self).__init__(CapacitorModel, CapacitorDto)

    def to_model(self, dto):
        return CapacitorModel(
            voltage=dto.voltage,
            tolerance=dto.tolerance,
            composition=dto.composition,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class CrystalOscillatorModelMapper(DtoModelMaper):

    def __init__(self):
        super(CrystalOscillatorModelMapper, self).__init__(CrystalOscillatorModel, CrystalOscillatorDto)

    def to_model(self, dto):
        return CrystalOscillatorModel(
            load_capacitance=dto.load_capacitance,
            frequency=dto.frequency,
            frequency_tolerance=dto.frequency_tolerance,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class DiodeRectifierModelMapper(DtoModelMaper):

    def __init__(self):
        super(DiodeRectifierModelMapper, self).__init__(DiodeRectifierModel, DiodeRectifierDto)

    def to_model(self, dto):
        return DiodeRectifierModel(
            forward_voltage=dto.forward_voltage,
            reverse_current_leakage=dto.reverse_current_leakage,
            max_forward_average_current=dto.max_forward_average_current,
            max_reverse_vrrm=dto.max_reverse_vrrm,
            diode_type=dto.diode_type,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class DiodeTVSModelMapper(DtoModelMaper):

    def __init__(self):
        super(DiodeTVSModelMapper, self).__init__(DiodeTVSModel, DiodeTVSDto)

    def to_model(self, dto):
        return DiodeTVSModel(
            voltage_reverse_standoff=dto.voltage_reverse_standoff,
            voltage_breakdown_min=dto.voltage_breakdown_min,
            voltage_clamping_max=dto.voltage_clamping_max,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class DiodeZenerModelMapper(DtoModelMaper):

    def __init__(self):
        super(DiodeZenerModelMapper, self).__init__(DiodeZenerModel, DiodeZenerDto)

    def to_model(self, dto):
        return DiodeZenerModel(
            tolerance=dto.tolerance,
            power_max=dto.power_max,
            voltage_forward=dto.voltage_forward,
            voltage_zener=dto.voltage_zener,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class FerriteBeadModelMapper(DtoModelMaper):

    def __init__(self):
        super(FerriteBeadModelMapper, self).__init__(FerriteBeadModel, FerriteBeadDto)

    def to_model(self, dto):
        return FerriteBeadModel(
            number_of_lines=dto.number_of_lines,
            dc_resistance=dto.dc_resistance,
            impedance_freq=dto.impedance_freq,
            current_rating=dto.current_rating,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class TransistorMosfetModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransistorMosfetModelMapper, self).__init__(TransistorMosfetModel, TransistorMosfetDto)

    def to_model(self, dto):
        return TransistorMosfetModel(
            rds_on=dto.rds_on,
            vgs_max=dto.vgs_max,
            vgs_th=dto.vgs_th,
            vds_max=dto.vds_max,
            ids_max=dto.ids_max,
            power_max=dto.power_max,
            channel_type=dto.channel_type,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class TransistorBjtModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransistorBjtModelMapper, self).__init__(TransistorBjtModel, TransistorBjtDto)

    def to_model(self, dto):
        return TransistorBjtModel(
            vce_sat_max=dto.vce_sat_max,
            hfe=dto.hfe,
            vce_max=dto.vce_max,
            ic_max=dto.ic_max,
            power_max=dto.power_max,
            bjt_type=dto.bjt_type,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class PowerInductorModelMapper(DtoModelMaper):

    def __init__(self):
        super(PowerInductorModelMapper, self).__init__(PowerInductorModel, PowerInductorDto)

    def to_model(self, dto):
        return PowerInductorModel(
            tolerance=dto.tolerance,
            resistance_dcr=dto.resistance_dcr,
            inductance_freq_test=dto.inductance_freq_test,
            current_rating=dto.current_rating,
            current_saturation=dto.current_saturation,
            core_material=dto.core_material,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class VoltageRegulatorDCDCModelMapper(DtoModelMaper):

    def __init__(self):
        super(VoltageRegulatorDCDCModelMapper, self).__init__(VoltageRegulatorDCDCModel, VoltageRegulatorDCDCDto)

    def to_model(self, dto):
        return VoltageRegulatorDCDCModel(
            voltage_input_min=dto.voltage_input_min,
            voltage_output_min_fixed=dto.voltage_output_min_fixed,
            voltage_output_max=dto.voltage_output_max,
            current_output=dto.current_output,
            frequency_switching=dto.frequency_switching,
            topology=dto.topology,
            output_type=dto.output_type,
            number_of_outputs=dto.number_of_outputs,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class VoltageRegulatorLinearModelMapper(DtoModelMaper):

    def __init__(self):
        super(VoltageRegulatorLinearModelMapper, self).__init__(VoltageRegulatorLinearModel, VoltageRegulatorLinearDto)

    def to_model(self, dto):
        return VoltageRegulatorLinearModel(
            gain_bandwith=dto.gain_bandwith,
            output_type=dto.output_type,
            voltage_output_min_fixed=dto.voltage_output_min_fixed,
            voltage_output_max=dto.voltage_output_max,
            voltage_dropout_max=dto.voltage_dropout_max,
            current_supply_max=dto.current_supply_max,
            current_output=dto.current_output,
            pssr=dto.pssr,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class MicrocontrollerModelMapper(DtoModelMaper):

    def __init__(self):
        super(MicrocontrollerModelMapper, self).__init__(MicrocontrollerModel, MicrocontrollerDto)

    def to_model(self, dto):
        return MicrocontrollerModel(
            core=dto.core,
            core_size=dto.core_size,
            speed=dto.speed,
            flash_size=dto.flash_size,
            ram_size=dto.ram_size,
            peripherals=dto.peripherals,
            connectivity=dto.connectivity,
            voltage_supply=dto.voltage_supply,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class OpAmpModelMapper(DtoModelMaper):

    def __init__(self):
        super(OpAmpModelMapper, self).__init__(OpAmpModel, OpAmpDto)

    def to_model(self, dto):
        return OpAmpModel(
            gain_bandwith=dto.gain_bandwith,
            output_type=dto.output_type,
            input_type=dto.input_type,
            amplifier_type=dto.amplifier_type,
            slew_rate=dto.slew_rate,
            voltage_supplies=dto.voltage_supplies,
            voltage_input_offset=dto.voltage_input_offset,
            current_output=dto.current_output,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class PotentiometerModelMapper(DtoModelMaper):

    def __init__(self):
        super(PotentiometerModelMapper, self).__init__(PotentiometerModel, PotentiometerDto)

    def to_model(self, dto):
        return PotentiometerModel(
            power_max=dto.power_max,
            tolerance=dto.tolerance,
            resistance_min=dto.resistance_min,
            resistance_max=dto.resistance_max,
            number_of_turns=dto.number_of_turns,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class MemoryModelMapper(DtoModelMaper):

    def __init__(self):
        super(MemoryModelMapper, self).__init__(MemoryModel, MemoryDto)

    def to_model(self, dto):
        return MemoryModel(
            technology=dto.technology,
            memory_type=dto.memory_type,
            size=dto.size,
            interface=dto.interface,
            clock_frequency=dto.clock_frequency,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class OptocouplerDigitalModelMapper(DtoModelMaper):

    def __init__(self):
        super(OptocouplerDigitalModelMapper, self).__init__(OptocouplerDigitalModel, OptocouplerDigitalDto)

    def to_model(self, dto):
        return OptocouplerDigitalModel(
            voltage_isolation=dto.voltage_isolation,
            voltage_saturation_max=dto.voltage_saturation_max,
            current_transfer_ratio_max=dto.current_transfer_ratio_max,
            current_transfer_ratio_min=dto.current_transfer_ratio_min,
            voltage_forward_typical=dto.voltage_forward_typical,
            voltage_output_max=dto.voltage_output_max,
            number_of_channels=dto.number_of_channels,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class OptocouplerLinearModelMapper(DtoModelMaper):

    def __init__(self):
        super(OptocouplerLinearModelMapper, self).__init__(OptocouplerLinearModel, OptocouplerLinearDto)

    def to_model(self, dto):
        return OptocouplerLinearModel(
            voltage_isolation=dto.voltage_isolation,
            transfer_gain=dto.transfer_gain,
            input_forward_voltage=dto.input_forward_voltage,
            servo_gain=dto.servo_gain,
            forward_gain=dto.forward_gain,
            non_linearity=dto.non_linearity,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class LedIndicatorModelMapper(DtoModelMaper):

    def __init__(self):
        super(LedIndicatorModelMapper, self).__init__(LedIndicatorModel, LedIndicatorDto)

    def to_model(self, dto):
        return LedIndicatorModel(
            forward_voltage=dto.forward_voltage,
            color=dto.color,
            lens_style=dto.lens_style,
            lens_transparency=dto.lens_transparency,
            dominant_wavelength=dto.dominant_wavelength,
            test_current=dto.test_current,
            lens_size=dto.lens_size,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class SwitchPushButtonModelMapper(DtoModelMaper):

    def __init__(self):
        super(SwitchPushButtonModelMapper, self).__init__(SwitchPushButtonModel, SwitchPushButtonDto)

    def to_model(self, dto):
        return SwitchPushButtonModel(
            function=dto.function,
            dc_voltage_rating=dto.dc_voltage_rating,
            ac_voltage_rating=dto.ac_voltage_rating,
            current_rating=dto.current_rating,
            circuit_type=dto.circuit_type,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class SwitchSwitchModelMapper(DtoModelMaper):

    def __init__(self):
        super(SwitchSwitchModelMapper, self).__init__(SwitchSwitchModel, SwitchSwitchDto)

    def to_model(self, dto):
        return SwitchSwitchModel(
            voltage_rating=dto.voltage_rating,
            current_rating=dto.current_rating,
            number_of_positions=dto.number_of_positions,
            circuit_type=dto.circuit_type,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class TransceiverModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransceiverModelMapper, self).__init__(TransceiverModel, TransceiverDto)

    def to_model(self, dto):
        return TransceiverModel(
            duplex=dto.duplex,
            data_rate=dto.data_rate,
            protocol=dto.protocol,
            voltage_supply=dto.voltage_supply,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


class ConnectorPcbModelMapper(DtoModelMaper):

    def __init__(self):
        super(ConnectorPcbModelMapper, self).__init__(ConnectorPcbModel, ConnectorPcbDto)

    def to_model(self, dto):
        return ConnectorPcbModel(
            orientation=dto.orientation,
            pitch=dto.pitch,
            voltage_rating=dto.voltage_rating,
            current_rating=dto.current_rating,
            number_of_rows=dto.number_of_rows,
            number_of_contacts=dto.number_of_contacts,
            value=dto.value,
            package=dto.package,
            description=dto.description,
            comment=dto.comment,
            is_through_hole=dto.is_through_hole,
            type=dto.type,
            mpn=dto.mpn,
            manufacturer=dto.manufacturer
        )


mapper_instances = [
    ResistorModelMapper(),
    CapactitorModelMapper(),
    CrystalOscillatorModelMapper(),
    DiodeRectifierModelMapper(),
    DiodeTVSModelMapper(),
    DiodeZenerModelMapper(),
    FerriteBeadModelMapper(),
    TransistorMosfetModelMapper(),
    TransistorBjtModelMapper(),
    PowerInductorModelMapper(),
    VoltageRegulatorDCDCModelMapper(),
    VoltageRegulatorLinearModelMapper(),
    MicrocontrollerModelMapper(),
    OpAmpModelMapper(),
    PotentiometerModelMapper(),
    MemoryModelMapper(),
    OptocouplerDigitalModelMapper(),
    OptocouplerLinearModelMapper(),
    LedIndicatorModelMapper(),
    SwitchPushButtonModelMapper(),
    SwitchSwitchModelMapper(),
    TransceiverModelMapper(),
    ConnectorPcbModelMapper()
]

model_to_dto_quick_dict = {}
dto_to_model_quick_dict = {}
for inst in mapper_instances:
    model_to_dto_quick_dict[inst.model_id] = inst
    dto_to_model_quick_dict[inst.dto_type] = inst


def get_mapper_for_dto(dto_type):
    global dto_to_model_quick_dict
    dto_t = type(dto_type)
    if dto_t in dto_to_model_quick_dict:
        return dto_to_model_quick_dict[dto_t]
    else:
        return None


def get_mapper_for_model(model_type):
    global model_to_dto_quick_dict
    model_t = model_type.__class__
    if model_t.__name__ in model_to_dto_quick_dict:
        return model_to_dto_quick_dict[model_t.__name__]
    else:
        return None
