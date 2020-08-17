import pytest

from dtos import component_model_mapper
from models import ResistorModel
from services.exceptions import InvalidComponentFieldsError, InvalidComponentTypeError


def __assert_base_component(result, expected):
    assert expected.description == result.description
    assert expected.value == result.value
    assert expected.package == result.package
    assert expected.comment == result.comment
    assert expected.type == result.type
    assert expected.is_through_hole == result.is_through_hole
    assert expected.mpn == result.mpn
    assert expected.manufacturer == result.manufacturer


def __get_generic_raw_resistor():
    return {
        "power_max": "100 mW",
        "tolerance": "1%",
        "description": "Thin Film Resistor 392 Ohms 1%",
        "value": "392 Ohms",
        "package": "0603 (1608 Metric)",
        "comment": "=Value",
        "type": "resistor",
        "is_through_hole": False,
        "mpn": "CRCW0603392RFKEAC",
        "manufacturer": "Vishay / Dale"
    }


def test_map_resistor_ok():
    raw = __get_generic_raw_resistor()

    model = ResistorModel(
        power_max='2 W',
        tolerance="20 %",
        description="Thin Film Resistor 392 Ohms 1%",
        value="392 Ohms",
        package="0603 (1608 Metric)",
        comment="=Value",
        type="resistor",
        is_through_hole=False,
        mpn="CRCW0603392RFKEAC",
        manufacturer="Vishay / Dale"
    )

    mapped = component_model_mapper.map_validate_raw(raw, pk_provided=False)
    __assert_base_component(mapped, model)


def test_map_model_to_raw_resistor_ok():
    model = ResistorModel(
        power_max='2 W',
        tolerance="20 %",
        description="Thin Film Resistor 392 Ohms 1%",
        value="392 Ohms",
        package="0603 (1608 Metric)",
        comment="=Value",
        type="resistor",
        is_through_hole=False,
        mpn="CRCW0603392RFKEAC",
        manufacturer="Vishay / Dale"
    )

    raw = component_model_mapper.map_model_to_raw(model)
    assert model.power_max == raw['power_max']
    assert model.tolerance == raw['tolerance']
    assert model.description == raw['description']
    assert model.value == raw['value']
    assert model.package == raw['package']
    assert model.comment == raw['comment']
    assert model.type == raw['type']
    assert model.is_through_hole == raw['is_through_hole']
    assert model.mpn == raw['mpn']
    assert model.manufacturer == raw['manufacturer']


def test_map_component_not_expected_field_ko():
    raw = __get_generic_raw_resistor()
    raw['thisfieldshouldtbepresent'] = "wololo"

    with pytest.raises(Exception) as e_info:
        component_model_mapper.map_validate_raw(raw, pk_provided=False)

    assert e_info.type is InvalidComponentFieldsError
    assert e_info.value.unrecognised_fields is not None
    assert len(e_info.value.unrecognised_fields) == 1
    assert e_info.value.unrecognised_fields[0] == 'thisfieldshouldtbepresent'


def test_map_component_not_expected_type_ko():
    raw = __get_generic_raw_resistor()
    raw['type'] = 'shouldnotexist'

    with pytest.raises(Exception) as e_info:
        component_model_mapper.map_validate_raw(raw, pk_provided=False)

    assert e_info.type is InvalidComponentTypeError

    # Try map without type
    del raw['type']
    with pytest.raises(Exception) as e_info:
        component_model_mapper.map_validate_raw(raw, pk_provided=False)

    assert e_info.type is InvalidComponentTypeError


def test_map_component_not_expected_field_type_ko():
    raw = __get_generic_raw_resistor()
    raw['power_max'] = 1.0
    with pytest.raises(Exception) as e_info:
        component_model_mapper.map_validate_raw(raw, pk_provided=False)

    assert e_info.type is InvalidComponentFieldsError
    assert e_info.value.unexpected_types is not None
    assert len(e_info.value.unexpected_types) == 1
    assert e_info.value.unexpected_types[0] == 'power_max'


def test_map_component_no_mandatory_field_ko():
    raw = __get_generic_raw_resistor()
    del raw['mpn']
    with pytest.raises(Exception) as e_info:
        component_model_mapper.map_validate_raw(raw, pk_provided=False)

    assert e_info.type is InvalidComponentFieldsError
    assert e_info.value.mandatory_missing is not None
    assert len(e_info.value.mandatory_missing) == 1
    assert e_info.value.mandatory_missing[0] == 'mpn'
