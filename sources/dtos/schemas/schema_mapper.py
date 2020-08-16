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


from dtos.components_dtos import ResistorDto, CapacitorDto, DiodeTVSDto, DiodeZenerDto, DiodeRectifierDto, \
    FerriteBeadDto, TransistorMosfetDto, PowerInductorDto, TransistorBjtDto, CrystalOscillatorDto, \
    VoltageRegulatorLinearDto, VoltageRegulatorDCDCDto, MicrocontrollerDto, OpAmpDto, PotentiometerDto, MemoryDto, \
    OptocouplerDigitalDto, OptocouplerLinearDto, LedIndicatorDto, SwitchSwitchDto, SwitchPushButtonDto, \
    ConnectorPcbDto, TransceiverDto, TransducerDto, InductorChokeDto, TransformerDto
from dtos.schemas.component_schemas import TransistorBjtSchema, CapacitorSchema, CrystalOscillatorSchema, \
    DiodeRectifierSchema, DiodeTVSSchema, DiodeZenerSchema, FerriteBeadSchema, TransistorMosfetSchema, \
    PowerInductorSchema, ResistorSchema, VoltageRegulatorDCDCSchema, VoltageRegulatorLinearSchema, \
    MicrocontrollerSchema, OpAmpSchema, PotentiometerSchema, MemorySchema, OptocouplerDigitalSchema, \
    OptocouplerLinearSchema, LedIndicatorSchema, SwitchPushButtonSchema, SwitchSwitchSchema, ConnectorPcbSchema, \
    TransceiverSchema, TransducerSchema, InductorChokeSchema, TransformerSchema
from models import ResistorModel, DiodeTVSModel, CapacitorModel, DiodeZenerModel, DiodeRectifierModel, \
    FerriteBeadModel, PowerInductorModel, CrystalOscillatorModel, TransistorBjtModel, TransistorMosfetModel, \
    VoltageRegulatorDCDCModel, VoltageRegulatorLinearModel, MicrocontrollerModel, OpAmpModel, PotentiometerModel, \
    MemoryModel, OptocouplerDigitalModel, OptocouplerLinearModel, LedIndicatorModel, ConnectorPcbModel, \
    SwitchPushButtonModel, SwitchSwitchModel, TransceiverModel, TransducerModel, InductorChokeModel
from models.transformer_model import TransformerModel


def get_schema_for_component_name(component_type):
    schema_map = {
        ResistorModel.__tablename__: ResistorSchema,
        CapacitorModel.__tablename__: CapacitorSchema,
        DiodeTVSModel.__tablename__: DiodeTVSSchema,
        DiodeZenerModel.__tablename__: DiodeZenerSchema,
        DiodeRectifierModel.__tablename__: DiodeRectifierSchema,
        FerriteBeadModel.__tablename__: FerriteBeadSchema,
        CrystalOscillatorModel.__tablename__: CrystalOscillatorSchema,
        TransistorBjtModel.__tablename__: TransistorBjtSchema,
        TransistorMosfetModel.__tablename__: TransistorMosfetSchema,
        PowerInductorModel.__tablename__: PowerInductorSchema,
        VoltageRegulatorDCDCModel.__tablename__: VoltageRegulatorDCDCSchema,
        VoltageRegulatorLinearModel.__tablename__: VoltageRegulatorLinearSchema,
        MicrocontrollerModel.__tablename__: MicrocontrollerSchema,
        OpAmpModel.__tablename__: OpAmpSchema,
        PotentiometerModel.__tablename__: PotentiometerSchema,
        MemoryModel.__tablename__: MemorySchema,
        OptocouplerDigitalModel.__tablename__: OptocouplerDigitalSchema,
        OptocouplerLinearModel.__tablename__: OptocouplerLinearSchema,
        LedIndicatorModel.__tablename__: LedIndicatorSchema,
        SwitchPushButtonModel.__tablename__: SwitchPushButtonSchema,
        SwitchSwitchModel.__tablename__: SwitchSwitchSchema,
        TransceiverModel.__tablename__: TransceiverSchema,
        ConnectorPcbModel.__tablename__: ConnectorPcbSchema,
        TransducerModel.__tablename__: TransducerSchema,
        InductorChokeModel.__tablename__: InductorChokeSchema,
        TransformerModel.__tablename__: TransformerSchema
    }
    return schema_map.get(component_type)


def get_schema_for_dto_class_name(schema):
    schema_map = {
        ResistorDto.__name__: ResistorSchema,
        CapacitorDto.__name__: CapacitorSchema,
        DiodeTVSDto.__name__: DiodeTVSSchema,
        DiodeZenerDto.__name__: DiodeZenerSchema,
        DiodeRectifierDto.__name__: DiodeRectifierSchema,
        FerriteBeadDto.__name__: FerriteBeadSchema,
        CrystalOscillatorDto.__name__: CrystalOscillatorSchema,
        TransistorBjtDto.__name__: TransistorBjtSchema,
        TransistorMosfetDto.__name__: TransistorMosfetSchema,
        PowerInductorDto.__name__: PowerInductorSchema,
        VoltageRegulatorDCDCDto.__name__: VoltageRegulatorDCDCSchema,
        VoltageRegulatorLinearDto.__name__: VoltageRegulatorLinearSchema,
        MicrocontrollerDto.__name__: MicrocontrollerSchema,
        OpAmpDto.__name__: OpAmpSchema,
        PotentiometerDto.__name__: PotentiometerSchema,
        MemoryDto.__name__: MemorySchema,
        OptocouplerDigitalDto.__name__: OptocouplerDigitalSchema,
        OptocouplerLinearDto.__name__: OptocouplerLinearSchema,
        LedIndicatorDto.__name__: LedIndicatorSchema,
        SwitchPushButtonDto.__name__: SwitchPushButtonSchema,
        SwitchSwitchDto.__name__: SwitchSwitchSchema,
        TransceiverDto.__name__: TransceiverSchema,
        ConnectorPcbDto.__name__: ConnectorPcbSchema,
        TransducerDto.__name__: TransducerSchema,
        InductorChokeDto.__name__: InductorChokeSchema,
        TransformerDto.__name__: TransformerSchema
    }
    return schema_map.get(schema)
