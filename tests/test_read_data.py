import os
from pathlib import Path

import pytest
import pandas as pd

import pytus2000 as tus
from pytus2000 import diary, individual


SKIP_CONDITION = not pytest.config.getoption("--runwithdataset")
SKIP_MESSAGE = "needs --runwithdataset option to run"

TEST_DIR = Path(os.path.abspath(__file__)).parent
PATH_TO_RESOURCES = TEST_DIR / 'resources'
PATH_TO_DIARY_FILE = TEST_DIR.parent / 'data' / 'tab' / 'diary_data_8.tab'
PATH_TO_DIARY_HEADER_FILE = PATH_TO_RESOURCES / 'diary_data_8_header.tab'
PATH_TO_INDIVIDUAL_FILE = TEST_DIR.parent / 'data' / 'tab' / 'Individual_data_5.tab'
PATH_TO_PATH_TO_INDIVIDUAL_HEADER_FILE = PATH_TO_RESOURCES / 'Individual_data_5_header.tab'


@pytest.fixture(params=[
    PATH_TO_DIARY_HEADER_FILE,
    pytest.mark.skipif(SKIP_CONDITION, reason=SKIP_MESSAGE)(PATH_TO_DIARY_FILE)
])
def path_to_diary_file(request):
    return request.param


@pytest.fixture(params=[
    PATH_TO_PATH_TO_INDIVIDUAL_HEADER_FILE,
    pytest.mark.skipif(SKIP_CONDITION, reason=SKIP_MESSAGE)(PATH_TO_INDIVIDUAL_FILE)
])
def path_to_individual_file(request):
    return request.param


class TestDiaryFile():

    def test_read_month(self, path_to_diary_file):
        data = tus.read_diary_file(path_to_diary_file)
        assert isinstance(data.DMONTH.dtype, pd.types.dtypes.CategoricalDtype)

    def test_read_activities(self, path_to_diary_file):
        data = tus.read_diary_file(path_to_diary_file)
        assert isinstance(data.ACT1_001.dtype, pd.types.dtypes.CategoricalDtype)

    def test_multi_index(self, path_to_diary_file):
        data = tus.read_diary_file(path_to_diary_file)
        assert data.index.names == ['SN1', 'SN2', 'SN3', 'SN4']


class TestIndividualFile():

    def test_multi_index(self, path_to_individual_file):
        data = tus.read_individual_file(path_to_individual_file)
        assert data.index.names == ['SN1', 'SN2', 'SN3']

    def test_read_proxy(self, path_to_individual_file):
        data = tus.read_individual_file(path_to_individual_file)
        assert isinstance(data.PROXYTYP.dtype, pd.types.dtypes.CategoricalDtype)

    def test_read_question1(self, path_to_individual_file):
        data = tus.read_individual_file(path_to_individual_file)
        assert isinstance(data.Q1A.dtype, pd.types.dtypes.CategoricalDtype)
