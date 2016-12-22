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


def test_module_has_variable_enum(datadict_module):
    datadict_module.Variable


def test_variable_enum_has_position(datadict_module):
    enum_members = [member for member in datadict_module.Variable]
    assert len(enum_members) > 0
    for enum_member in enum_members:
        enum_member.position


def test_variable_enum_has_label(datadict_module):
    enum_members = [member for member in datadict_module.Variable]
    assert len(enum_members) > 0
    for enum_member in enum_members:
        enum_member.label
