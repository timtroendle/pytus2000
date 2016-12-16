from collections import namedtuple, OrderedDict
from itertools import dropwhile, groupby
from pathlib import Path
import os

import click

PATH_FOR_GENERATED_CODE = Path(os.path.abspath(__file__)).parent.parent / 'generated'
VARIABLE_SECTION_START = 'Pos. = '
VARIABLE_NAME_FIELD = 'Variable = '
VARIABLE_LABEL_FIELD = 'Variable label = '
VALUE_FIELD = 'Value = '
VALUE_LABEL_FIELD = 'Label = '

Variable = namedtuple('Variable', ['id', 'name', 'label', 'values'])


class PathlibParamType(click.ParamType):
    name = 'Path'

    def convert(self, value, param, ctx):
        path = Path(value)
        if not path.exists():
            self.fail('Path "{}" does not exist.'.format(value))
        return path


@click.command(name='datadict-translator')
@click.argument('datadict', type=PathlibParamType())
def generate_code(datadict):
    PATH_FOR_GENERATED_CODE.mkdir(exist_ok=True)
    variables = parse_data_dictionary(datadict)
    write_data_dictionary(variables, PATH_FOR_GENERATED_CODE / 'datadict.py')


def parse_data_dictionary(path_to_file):
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
    lines = [
        '"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""',
        'from enum import Enum',
        '',
        '',
        'class Variable(Enum):'
    ]
    for i, variable in enumerate(variables):
        lines.append('    {} = {}'.format(variable.name.upper(), i + 1))
    variable_cache = []
    for variable in filter(_variable_has_values, variables):
        lines.append('')
        lines.append('')
        if len(_variables_with_same_value(variable_cache)(variable)) == 0:
            lines.append('class {}(Enum):'.format(_convert_name(variable.name)))
            for value, label in variable.values.items():
                lines.append("    {} = '{}'".format(_convert_name(label.upper()), value))
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
    value_lines = filter(lambda line: line.startswith(VALUE_FIELD), variable_section)
    return Variable(
        id=int(position.split(VARIABLE_SECTION_START)[1]),
        name=name.split(VARIABLE_NAME_FIELD)[1],
        label=label.split(VARIABLE_LABEL_FIELD)[1],
        values=_parse_variable_values(value_lines)
    )


def _parse_variable_values(value_lines):
    values = [
        (value.split(VALUE_FIELD)[1], label.split(VALUE_LABEL_FIELD)[1])
        for value, label in (line.split('\t') for line in value_lines)
    ]
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


def _variables_with_same_value(reference_variables):
    def _variables_with_same_value(variable):
        return [var for var in reference_variables if var.values == variable.values]
    return _variables_with_same_value


def _convert_name(name):
    return name.upper().replace(' ', '_')


if __name__ == '__main__':
    generate_code()
