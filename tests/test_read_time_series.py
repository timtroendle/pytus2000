import os
from pathlib import Path

import pytest
import pandas as pd

import pytus2000 as tus
from pytus2000 import diary, cache


SKIP_CONDITION = not pytest.config.getoption("--runwithdataset")
SKIP_MESSAGE = "needs --runwithdataset option to run"

TEST_DIR = Path(os.path.abspath(__file__)).parent
PATH_TO_RESOURCES = TEST_DIR / 'resources'
PATH_TO_DIARY_FILE = TEST_DIR.parent / 'data' / 'tab' / 'diary_data_8.tab'


@pytest.fixture(params=[
    pytest.mark.skipif(SKIP_CONDITION, reason=SKIP_MESSAGE)(PATH_TO_DIARY_FILE)
])
def path_to_diary_file(request):
    return request.param


class TestDiaryFile():

    def test_columns(self, path_to_diary_file):
        data = tus.read_diary_file_as_timeseries(path_to_diary_file)
        assert all(data.columns == ['activity', 'location', 'secondary_activity', 'who_with_adult0',
                                    'who_with_adult1', 'who_with_adult2', 'who_with_adult3',
                                    'who_with_adult4', 'who_with_adult5', 'who_with_adult6',
                                    'who_with_child0', 'who_with_child1', 'who_with_child2',
                                    'who_with_child3', 'who_with_child4', 'who_with_child5'])

    def test_multi_index(self, path_to_diary_file):
        data = tus.read_diary_file_as_timeseries(path_to_diary_file)
        assert data.index.names == ['SN1', 'SN2', 'SN3', 'SN4', 'time_of_day']
