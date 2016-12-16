"""The functions in this module generate Python code from data dictionaries.

This file is not intended to be used by user of pytus2000, instead it creates
large parts of pytus2000 code automatically.
"""
from collections import namedtuple, OrderedDict
from itertools import dropwhile, groupby
from pathlib import Path
import os

import click

PATH_FOR_GENERATED_CODE = Path(os.path.abspath(__file__)).parent.parent / 'pytus2000' / 'datadicts'
VARIABLE_SECTION_START = 'Pos. = '
VARIABLE_NAME_FIELD = 'Variable = '
VARIABLE_LABEL_FIELD = 'Variable label = '
MISSING_VALUE_FIELD = 'SPSS user missing value = '
VALUE_FIELD = 'Value = '
VALUE_LABEL_FIELD = 'Label = '
CHAR_PRECEDING_NUMBER = 'N'

Variable = namedtuple('Variable', ['id', 'name', 'label', 'values'])

FILE_MAPPING = {
    Path('diary_data_8_episode_UKDA_Data_Dictionary.txt'): Path('diaryepisode.py'),
    Path('diary_data_8_UKDA_Data_Dictionary.txt'): Path('diary.py'),
    Path('hhld_data_6_UKDA_Data_Dictionary.txt'): Path('household.py'),
    Path('Individual_data_5_UKDA_Data_Dictionary.txt'): Path('individual.py'),
    Path('weight_diary_person_UKDA_Data_Dictionary.txt'): Path('weightdiary.py'),
    Path('worksheet_data_3_UKDA_Data_Dictionary.txt'): Path('worksheet.py')
}

CHARACTER_MAPPING = OrderedDict([ # these characters in labels will be mapped to their counterpart
    (' – ', '_'),
    ('–', '_'),
    ('-', '_'),
    (' ', '_'),
    ("'", '_'),
    ('.', '_'),
    (',', '_'),
    ('%', 'percent'),
    ('?', ''),
    ('(S)', ''),
    ('(', ''),
    (')', ''),
    ('£', 'GBP'),
    (':', ''),
    (';', ''),
    ('+', 'plus'),
    ('&', 'and'),
    ('/', ''),
    ('<', 'smaller'),
    ('<=', 'smallerequal'),
    ('>', 'greater'),
    ('>=', 'greaterequal'),
    ('=', 'equal'),
    ('@', 'AT')
])


class _PathToDataDictsParamType(click.ParamType):
    name = 'PathToDataDicts'

    def convert(self, value, param, ctx):
        path = Path(value)
        if not path.exists():
            self.fail('Path "{}" does not exist.'.format(value))
        if any(path / file_path not in path.glob('*') for file_path in FILE_MAPPING.keys()):
            missing_files = [path / file_path for file_path in FILE_MAPPING.keys()
                             if path / file_path not in path.glob('*')]
            self.fail("There are not all necessary files in the folder '{}'.\n \
                      Missing: {}.".format(path, missing_files))
        return path


@click.command(name='datadict-translator')
@click.argument('datadicts', type=_PathToDataDictsParamType())
def generate_code(datadicts):
    """Generates PyTUS2000 source code.

    \b
    Parameters:
        datadicts:  The folder containing all data dictionaries to be translated.
                    Must be in plain text; rtf will fail.
    """
    PATH_FOR_GENERATED_CODE.mkdir(exist_ok=True)
    for original, generated in FILE_MAPPING.items():
        original = datadicts / original
        generated = PATH_FOR_GENERATED_CODE / generated
        print('Converting {} to {}...'.format(original, generated))
        variables = parse_data_dictionary(original)
        write_data_dictionary(variables, generated)
    print('All Done.')


def parse_data_dictionary(path_to_file):
    """Parses a data dictionary file from the study.

    This function can't handle with the rtf files as provided in the study. They have to
    be converted to plain text before.

    Parameters:
        * path_to_file: a pathlib.Path to the file to be parsed; must be plain text

    Returns:
        all variables found in the data dictionary
    """
    with path_to_file.open('r') as txt_file:
        lines = txt_file.readlines()
    lines = filter(lambda line: line is not '\n', lines)
    lines = dropwhile(lambda line: not line.startswith(VARIABLE_SECTION_START), lines)
    lines = (line.rstrip('\n') for line in lines)
    variable_sections = _variable_section_generator(lines)
    variables = [_parse_variable(variable_section)
                 for variable_section in variable_sections]
    return variables


def write_data_dictionary(variables, path_to_file):
    """Writes data dictionary variables to Python source code.

    Parameters:
        * variables: all variables to be written
        * path_to_file: a pathlib.Path to the file to be written.
    """
    lines = [
        '"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""',
        'from enum import Enum',
        '',
        '',
        'class Variable(Enum):'
    ]
    for i, variable in enumerate(variables):
        lines.append('    {} = {}'.format(_convert_name(variable.name), i + 1))
    variable_cache = []
    for variable in filter(_variable_is_usable, filter(_variable_has_values, variables)):
        lines.append('')
        lines.append('')
        if len(_variables_with_same_value(variable_cache)(variable)) == 0:
            lines.append('class {}(Enum):'.format(_convert_name(variable.name)))
            label_cache = []
            for value, label in variable.values.items():
                if label in label_cache:
                    new_label = label + '2'
                    print('Duplicate label: {} renamed to {}'.format(label, new_label))
                    label = new_label
                lines.append("    {} = '{}'".format(_convert_name(label.upper()), value))
                label_cache.append(label)
            variable_cache.append(variable)
        else:
            variable_with_same_values = _variables_with_same_value(variable_cache)(variable)[0]
            lines.append('{} = {}'.format(
                _convert_name(variable.name),
                _convert_name(variable_with_same_values.name))
            )
    lines = (line + '\n' for line in lines)
    with path_to_file.open('w') as f1:
        f1.writelines(lines)


def _parse_variable(variable_section):
    variable_section = list(variable_section)
    position, name, label = variable_section[0].split('\t')
    missing_values = _parse_missing_values(variable_section)
    value_lines = filter(lambda line: line.startswith(VALUE_FIELD), variable_section)
    return Variable(
        id=int(position.split(VARIABLE_SECTION_START)[1]),
        name=name.split(VARIABLE_NAME_FIELD)[1],
        label=label.split(VARIABLE_LABEL_FIELD)[1],
        values=_parse_variable_values(value_lines, missing_values)
    )


def _parse_missing_values(variable_section):
    if any(line.startswith(MISSING_VALUE_FIELD) for line in variable_section):
        line = [line for line in variable_section if line.startswith(MISSING_VALUE_FIELD)][0]
        return (value.strip() for value in line.strip().split(MISSING_VALUE_FIELD)[1].split('and'))
    else:
        return []


def _parse_variable_values(value_lines, missing_values):
    values = [
        (value.split(VALUE_FIELD)[1], label.split(VALUE_LABEL_FIELD)[1])
        for value, label in (line.split('\t') for line in value_lines)
    ]
    for i, missing_value in enumerate(missing_values):
        values.append((missing_value, 'missing{}'.format(i + 1)))
    return OrderedDict(values) if len(values) > 0 else None


def _variable_section_generator(lines):
    variable_section = []
    for line in lines:
        if line.startswith(VARIABLE_SECTION_START) and len(variable_section) > 0:
            yield variable_section
            variable_section = []
        variable_section.append(line)
    yield variable_section


def _variable_has_values(variable):
    return variable.values is not None


def _variable_is_usable(variable):
    # if there is only one value, it is very likely, that not all values are defined
    # if there are three values and they do not contain '1', they are likely unusable
    return len(variable.values) > 1 and (len(variable.values) > 3 or '1' in variable.values.keys())


def _variables_with_same_value(reference_variables):
    def _variables_with_same_value(variable):
        return [var for var in reference_variables if var.values == variable.values]
    return _variables_with_same_value


def _convert_name(name):
    if any(name.startswith(str(i)) for i in range(10)):
        name = CHAR_PRECEDING_NUMBER + name
    for invalid_char, valid_str in CHARACTER_MAPPING.items():
        name = name.replace(invalid_char, valid_str)
    return name.upper()


if __name__ == '__main__':
    generate_code()
