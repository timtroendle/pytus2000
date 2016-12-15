from pathlib import Path
import sys
import os

import pytest

sys.path.append('./scripts/')
from generate_code import DataDictionaryParser, Variable

PATH_TO_TEST_DATA_DICTIONARY = (Path(os.path.abspath(__file__)).parent / 'resources' /
                                'test_data_dictionary.txt')
PATH_TO_ORIGINAL_DATA_DICTIONARY = (Path(os.path.abspath(__file__)).parent / 'resources' /
                                    'orig_data_dictionary.txt')


@pytest.fixture
def parser():
    return DataDictionaryParser(PATH_TO_TEST_DATA_DICTIONARY)


@pytest.fixture
def original_file_parser():
    return DataDictionaryParser(PATH_TO_ORIGINAL_DATA_DICTIONARY)


class TestsUsingTestDataDictionary():

    def test_detects_all_variables(self, parser):
        assert len(parser.variables) == 4

    def test_detects_first_variable(self, parser):
        assert parser.variables[0] == Variable(id=1, name='v1', label='variable label 1',
                                               values=None)

    def test_detects_second_variable(self, parser):
        assert parser.variables[1] == Variable(id=2, name='v2', label='variable label 2',
                                               values=None)

    def test_detects_third_variable(self, parser):
        assert parser.variables[2] == Variable(
            id=3,
            name='v3',
            label='variable label 3',
            values={
                '0': 'label1',
                '1': 'label2',
                '2': 'label3'
            }
        )

    def test_detects_forth_variable(self, parser):
        assert parser.variables[3] == Variable(
            id=4,
            name='v4',
            label='variable label 4',
            values={
                '2.2': 'some label',
                '2.3': 'some other label'
            }
        )


@pytest.mark.skipif(
    not PATH_TO_ORIGINAL_DATA_DICTIONARY.exists(),
    reason='Original Data Dictionary must exist.'
)
class TestsUsingOriginalDataDictionary():

    def test_detects_all_variables_in_original(self, original_file_parser):
        assert len(original_file_parser.variables) == 3164
