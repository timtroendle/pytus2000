import os
from pathlib import Path

import pytest

import pytus2000
from pytus2000.datadicts.diary import DMONTH, ACT1_001


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
        data = pytus2000.read_diary_file(path_to_diary_file)
        assert data.DMONTH.dtype == DMONTH

    def test_read_activities(self, path_to_diary_file):
        data = pytus2000.read_diary_file(path_to_diary_file)
        assert data.ACT1_001.dtype == ACT1_001
