from pathlib import Path
import sys
import os

import pytest

sys.path.append('./scripts/')
from generate_code import Variable, parse_data_dictionary, write_data_dictionary

PATH_TO_TEST_FOLDER = Path(os.path.abspath(__file__)).parent
PATH_TO_RESOURCES = PATH_TO_TEST_FOLDER / 'resources'
PATH_TO_DATA = PATH_TO_TEST_FOLDER.parent / 'data'
PATH_TO_TEST_DATA_DICTIONARY = PATH_TO_RESOURCES / 'test_data_dictionary.txt'
PATH_TO_ORIGINAL_DATA_DICTIONARY = (PATH_TO_DATA / 'mrdoc' / 'allissue' /
                                    'diary_data_8_UKDA_Data_Dictionary.txt')
PATH_TO_EXPECTED_TEST_DATA_DICTIONARY = PATH_TO_RESOURCES / 'resulting_datadicts.py'

dataset = pytest.mark.skipif(
    not pytest.config.getoption("--runwithdataset"),
    reason="need --runwithdataset option to run"
)


class TestsParsingTestDataDictionary():

    def test_detects_all_variables(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert len(variables) == 6

    def test_detects_first_variable(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert variables[0] == Variable(pos=1, name='v1', label='variable label 1',
                                        values=None)

    def test_detects_second_variable(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert variables[1] == Variable(pos=2, name='@v2', label='variable label 2',
                                        values=None)

    def test_detects_third_variable(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert variables[2] == Variable(
            pos=3,
            name='v3',
            label='variable label 3',
            values={
                '0': 'label1',
                '1': 'label2',
                '2': 'label3',
                '99': 'missing1'
            }
        )

    def test_detects_forth_variable(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert variables[3] == Variable(
            pos=4,
            name='v4',
            label='variable label 4',
            values={
                '1.1': 'label',
                '2.2': '@some label',
                '2.3': '1some other label',
                '2.4': '@some label',
                '-1': 'missing1',
                '-9': 'missing2'
            }
        )

    def test_detects_fifth_variable(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert variables[4] == Variable(
            pos=5,
            name='v5',
            label='variable label 5',
            values={
                '0': 'label1',
                '1': 'label2',
                '2': 'label3',
                '99': 'missing1'
            }
        )

    def test_detects_sixth_variable(self):
        variables = parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY)
        assert variables[5] == Variable(
            pos=6,
            name='v6',
            label='variable label 6',
            values={
                '-9': 'invalid1',
                '-8': 'invalid2',
                '999999': 'invalid3',
            }
        )


@dataset
class TestsParsingOriginalDataDictionary():

    def test_detects_all_variables_in_original(self):
        variables = parse_data_dictionary(PATH_TO_ORIGINAL_DATA_DICTIONARY)
        assert len(variables) == 3164


class TestGeneratingPythonDatadicts():

    def test_creates_data_dict_correctly(self, tmpdir):
        tmpdir_path = Path(str(tmpdir))
        path_to_file = tmpdir_path / 'generated_file.py'
        write_data_dictionary(
            variables=parse_data_dictionary(PATH_TO_TEST_DATA_DICTIONARY),
            path_to_file=path_to_file
        )
        self.assert_equal_files(path_to_file, PATH_TO_EXPECTED_TEST_DATA_DICTIONARY)

    def assert_equal_files(self, path_to_file, path_to_expected_file):
        with path_to_file.open('r') as file1, path_to_expected_file.open('r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            for line1, line2 in zip(lines1[1:], lines2[1:]):
                assert line1 == line2
            assert len(lines1) == len(lines2), 'Files do not have same size.'
