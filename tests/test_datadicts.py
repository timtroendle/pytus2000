import pytest

from pytus2000 import diary, diaryepisode, individual, household, weightdiary, worksheet


@pytest.fixture(params=[
    diary,
    diaryepisode,
    individual,
    household,
    weightdiary,
    worksheet
])
def datadict_module(request):
    return request.param


@pytest.fixture(params=[
    diary,
    diaryepisode,
    individual,
    household,
    worksheet
])
def datadict_module_with_variable_enums(request):
    return request.param


@pytest.fixture
def variable_enum_members(datadict_module):
    return [member for member in datadict_module.Variable]


@pytest.fixture
def variable_enums(datadict_module_with_variable_enums):
    enums = []
    for member in datadict_module_with_variable_enums.Variable:
        try:
            datadict_module_with_variable_enums.__dict__[member.name]
            enums.append(datadict_module_with_variable_enums.__dict__[member.name])
        except KeyError:
            pass # nothing to do; there is no enum
    return enums


def test_module_has_variable_enum(datadict_module):
    datadict_module.Variable


def test_variable_enum_is_not_empty(variable_enum_members):
    assert len(variable_enum_members) > 0


def test_variable_enum_has_position(variable_enum_members):
    for variable_enum_member in variable_enum_members:
        variable_enum_member.position


def test_variable_enum_has_label(variable_enum_members):
    for variable_enum_member in variable_enum_members:
        variable_enum_member.label


def test_variable_enum_is_ordered_by_position(variable_enum_members):
    assert ((variable_enum_members[0] < variable_enum_members[-1]) ==
            (variable_enum_members[0].position < variable_enum_members[-1].position))


def test_module_has_variable_enums(variable_enums):
    assert len(variable_enums) > 0


def test_variable_enums_are_ordered_by_value(variable_enums):
    for enum in variable_enums:
        members = [member for member in enum]
        assert (members[0] < members[-1]) == (members[0].value < members[-1].value)
