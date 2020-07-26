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


from dtos.components_dtos import ResistorDto, CapacitorCeramicDto, CrystalOscillatorDto, DiodeRectifierDto, DiodeTVSDto, \
    DiodeZenerDto, FerriteBeadDto, TransistorMosfetDto, TransistorBjtDto, PowerInductorDto, VoltageRegulatorDCDCDto, \
    VoltageRegulatorLinearDto, MicrocontrollerDto, OpAmpDto, PotentiometerDto, MemoryDto, OptocouplerDigitalDto, \
    OptocouplerLinearDto, LedIndicatorDto, SwitchPushButtonDto, SwitchSwitchDto, TransceiverDto, ConnectorPcbDto, \
    TransducerDto, InductorChokeDto, TransformerDto, CapacitorElectrolyticDto, CapacitorTantalumDto, \
    TransistorArrayMosfetDto, OscillatorOscillatorDto
from models import ResistorModel, CrystalOscillatorModel, DiodeRectifierModel, DiodeZenerModel, \
    DiodeTVSModel, FerriteBeadModel, TransistorMosfetModel, TransistorBjtModel, PowerInductorModel, \
    VoltageRegulatorDCDCModel, VoltageRegulatorLinearModel, MicrocontrollerModel, OpAmpModel, PotentiometerModel, \
    MemoryModel, OptocouplerDigitalModel, OptocouplerLinearModel, SwitchPushButtonModel, SwitchSwitchModel, \
    TransceiverModel, ConnectorPcbModel, LedIndicatorModel, InductorChokeModel, TransducerModel, TransformerModel, \
    CapacitorCeramicModel, CapacitorElectrolyticModel, CapacitorTantalumModel, TransistorArrayMosfetModel, \
    OscillatorOscillatorModel


class DtoModelMaper:

    def __init__(self, model_type, dto_type):
        self.model_id = model_type.__name__
        self.model_type = model_type
        self.dto_type = dto_type

    def to_dto(self, model):
        return self.dto_type(**model.__dict__)

    def to_model(self, dto):
        return self.model_type(**dto.__dict__)


class ResistorModelMapper(DtoModelMaper):

    def __init__(self):
        super(ResistorModelMapper, self).__init__(ResistorModel, ResistorDto)


class CrystalOscillatorModelMapper(DtoModelMaper):

    def __init__(self):
        super(CrystalOscillatorModelMapper, self).__init__(CrystalOscillatorModel, CrystalOscillatorDto)


class DiodeRectifierModelMapper(DtoModelMaper):

    def __init__(self):
        super(DiodeRectifierModelMapper, self).__init__(DiodeRectifierModel, DiodeRectifierDto)


class DiodeTVSModelMapper(DtoModelMaper):

    def __init__(self):
        super(DiodeTVSModelMapper, self).__init__(DiodeTVSModel, DiodeTVSDto)


class DiodeZenerModelMapper(DtoModelMaper):

    def __init__(self):
        super(DiodeZenerModelMapper, self).__init__(DiodeZenerModel, DiodeZenerDto)


class FerriteBeadModelMapper(DtoModelMaper):

    def __init__(self):
        super(FerriteBeadModelMapper, self).__init__(FerriteBeadModel, FerriteBeadDto)


class TransistorMosfetModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransistorMosfetModelMapper, self).__init__(TransistorMosfetModel, TransistorMosfetDto)


class TransistorBjtModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransistorBjtModelMapper, self).__init__(TransistorBjtModel, TransistorBjtDto)


class PowerInductorModelMapper(DtoModelMaper):

    def __init__(self):
        super(PowerInductorModelMapper, self).__init__(PowerInductorModel, PowerInductorDto)


class VoltageRegulatorDCDCModelMapper(DtoModelMaper):

    def __init__(self):
        super(VoltageRegulatorDCDCModelMapper, self).__init__(VoltageRegulatorDCDCModel, VoltageRegulatorDCDCDto)


class VoltageRegulatorLinearModelMapper(DtoModelMaper):

    def __init__(self):
        super(VoltageRegulatorLinearModelMapper, self).__init__(VoltageRegulatorLinearModel, VoltageRegulatorLinearDto)


class MicrocontrollerModelMapper(DtoModelMaper):

    def __init__(self):
        super(MicrocontrollerModelMapper, self).__init__(MicrocontrollerModel, MicrocontrollerDto)


class OpAmpModelMapper(DtoModelMaper):

    def __init__(self):
        super(OpAmpModelMapper, self).__init__(OpAmpModel, OpAmpDto)


class PotentiometerModelMapper(DtoModelMaper):

    def __init__(self):
        super(PotentiometerModelMapper, self).__init__(PotentiometerModel, PotentiometerDto)


class MemoryModelMapper(DtoModelMaper):

    def __init__(self):
        super(MemoryModelMapper, self).__init__(MemoryModel, MemoryDto)


class OptocouplerDigitalModelMapper(DtoModelMaper):

    def __init__(self):
        super(OptocouplerDigitalModelMapper, self).__init__(OptocouplerDigitalModel, OptocouplerDigitalDto)


class OptocouplerLinearModelMapper(DtoModelMaper):

    def __init__(self):
        super(OptocouplerLinearModelMapper, self).__init__(OptocouplerLinearModel, OptocouplerLinearDto)


class LedIndicatorModelMapper(DtoModelMaper):

    def __init__(self):
        super(LedIndicatorModelMapper, self).__init__(LedIndicatorModel, LedIndicatorDto)


class SwitchPushButtonModelMapper(DtoModelMaper):

    def __init__(self):
        super(SwitchPushButtonModelMapper, self).__init__(SwitchPushButtonModel, SwitchPushButtonDto)


class SwitchSwitchModelMapper(DtoModelMaper):

    def __init__(self):
        super(SwitchSwitchModelMapper, self).__init__(SwitchSwitchModel, SwitchSwitchDto)


class TransceiverModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransceiverModelMapper, self).__init__(TransceiverModel, TransceiverDto)


class ConnectorPcbModelMapper(DtoModelMaper):

    def __init__(self):
        super(ConnectorPcbModelMapper, self).__init__(ConnectorPcbModel, ConnectorPcbDto)


class TransducerModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransducerModelMapper, self).__init__(TransducerModel, TransducerDto)


class InductorChokeModelMapper(DtoModelMaper):

    def __init__(self):
        super(InductorChokeModelMapper, self).__init__(InductorChokeModel, InductorChokeDto)


class TransformerModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransformerModelMapper, self).__init__(TransformerModel, TransformerDto)


class CapacitorCeramicModelMapper(DtoModelMaper):

    def __init__(self):
        super(CapacitorCeramicModelMapper, self).__init__(CapacitorCeramicModel, CapacitorCeramicDto)


class CapacitorElectrolyticModelMapper(DtoModelMaper):

    def __init__(self):
        super(CapacitorElectrolyticModelMapper, self).__init__(CapacitorElectrolyticModel, CapacitorElectrolyticDto)


class CapacitorTantalumModelMapper(DtoModelMaper):

    def __init__(self):
        super(CapacitorTantalumModelMapper, self).__init__(CapacitorTantalumModel, CapacitorTantalumDto)


class TransistorArrayMosfetModelMapper(DtoModelMaper):

    def __init__(self):
        super(TransistorArrayMosfetModelMapper, self).__init__(TransistorArrayMosfetModel, TransistorArrayMosfetDto)


class OscillatorOscillatorModelMapper(DtoModelMaper):

    def __init__(self):
        super(OscillatorOscillatorModelMapper, self).__init__(OscillatorOscillatorModel, OscillatorOscillatorDto)


mapper_instances = [
    ResistorModelMapper(),
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
    ConnectorPcbModelMapper(),
    TransducerModelMapper(),
    InductorChokeModelMapper(),
    TransformerModelMapper(),
    CapacitorCeramicModelMapper(),
    CapacitorElectrolyticModelMapper(),
    CapacitorTantalumModelMapper(),
    TransistorArrayMosfetModelMapper(),
    OscillatorOscillatorModelMapper()
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
