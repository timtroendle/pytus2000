import os
from pathlib import Path

import pytest
import pandas as pd

import pytus2000 as tus
from pytus2000 import diary


SKIP_CONDITION = not pytest.config.getoption("--runwithdataset")
SKIP_MESSAGE = "needs --runwithdataset option to run"

TEST_DIR = Path(os.path.abspath(__file__)).parent
PATH_TO_RESOURCES = TEST_DIR / 'resources'
PATH_TO_DIARY_FILE = TEST_DIR.parent / 'data' / 'tab' / 'diary_data_8.tab'
PATH_TO_DIARY_HEADER_FILE = TEST_DIR / 'resources' / 'diary_data_8_header.tab'


@pytest.fixture(params=[
    PATH_TO_DIARY_HEADER_FILE,
    pytest.mark.skipif(SKIP_CONDITION, reason=SKIP_MESSAGE)(PATH_TO_DIARY_FILE)
])
def path_to_diary_file(request):
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
