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


from dtos.component_dtos import ResistorDto, CapacitorDto, DiodeTVSDto, DiodeZenerDto, DiodeRectifierDto, \
    FerriteBeadDto, MosfetTransistorDto, PowerInductorDto, BjtTransistorDto, CrystalOscillatorDto
from dtos.schemas.component_schemas import BjtTransistorSchema, CapacitorSchema, CrystalOscillatorSchema, \
    DiodeRectifierSchema, DiodeTVSSchema, DiodeZenerSchema, FerriteBeadSchema, MosfetTransistorSchema, \
    PowerInductorSchema, ResistorSchema


def get_schema_for_dto(component_type):
    schema_map = {
        "resistor": ResistorSchema,
        "capacitor": CapacitorSchema,
        "diode_tvs": DiodeTVSSchema,
        "diode_zener": DiodeZenerSchema,
        "diode_rectifier": DiodeRectifierSchema,
        "ferrite_bead" : FerriteBeadSchema,
        "crystal_oscillator": CrystalOscillatorSchema,
        "bjt_transistor": BjtTransistorSchema,
        "mosfet_transistor": MosfetTransistorSchema,
        "power_inductor": PowerInductorSchema
    }
    return schema_map.get(component_type)


def get_dto_for_schema(schema):

    schema_map = {
        ResistorDto.__name__: ResistorSchema,
        CapacitorDto.__name__: CapacitorSchema,
        DiodeTVSDto.__name__: DiodeTVSSchema,
        DiodeZenerDto.__name__: DiodeZenerSchema,
        DiodeRectifierDto.__name__: DiodeRectifierSchema,
        FerriteBeadDto.__name__: FerriteBeadSchema,
        CrystalOscillatorDto.__name__: CrystalOscillatorSchema,
        BjtTransistorDto.__name__: BjtTransistorSchema,
        MosfetTransistorDto.__name__: MosfetTransistorSchema,
        PowerInductorDto.__name__: PowerInductorSchema,
    }
    return schema_map.get(schema)
