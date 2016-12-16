import os
from pathlib import Path

import pytus2000
from pytus2000.datadicts.diary import DMONTH, ACT1_001

TEST_DIR = Path(os.path.abspath(__file__)).parent
PATH_TO_RESOURCES = TEST_DIR / 'resources'
PATH_TO_DIARY_FILE = TEST_DIR.parent / 'data' / 'tab' / 'diary_data_8.tab'


class TestDiaryFile():

    def test_read_month(self):
        data = pytus2000.read_diary_file(PATH_TO_DIARY_FILE)
        assert data.DMONTH.dtype == DMONTH

    def test_read_activities(self):
        data = pytus2000.read_diary_file(PATH_TO_DIARY_FILE)
        assert data.ACT1_001.dtype == ACT1_001
