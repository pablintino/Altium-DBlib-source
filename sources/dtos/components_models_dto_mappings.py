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
    DiodeZenerDto, FerriteBeadDto, MosfetTransistorDto, BjtTransistorDto, PowerInductorDto
from models import ResistorModel, CapacitorModel, CrystalOscillatorModel, DiodeRectifierModel, DiodeZenerModel, \
    DiodeTVSModel, FerriteBeadModel, MosfetTransistorModel, BjtTransistorModel, PowerInductorModel


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


class MosfetTransistorModelMapper(DtoModelMaper):

    def __init__(self):
        super(MosfetTransistorModelMapper, self).__init__(MosfetTransistorModel, MosfetTransistorDto)

    def to_model(self, dto):
        return MosfetTransistorModel(
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


class BjtTransistorModelMapper(DtoModelMaper):

    def __init__(self):
        super(BjtTransistorModelMapper, self).__init__(BjtTransistorModel, BjtTransistorDto)

    def to_model(self, dto):
        return BjtTransistorModel(
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


mapper_instances = [
    ResistorModelMapper(),
    CapactitorModelMapper(),
    CrystalOscillatorModelMapper(),
    DiodeRectifierModelMapper(),
    DiodeTVSModelMapper(),
    DiodeZenerModelMapper(),
    FerriteBeadModelMapper(),
    MosfetTransistorModelMapper(),
    BjtTransistorModelMapper(),
    PowerInductorModelMapper()
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
