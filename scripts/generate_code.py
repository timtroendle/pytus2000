from collections import namedtuple, OrderedDict
from itertools import dropwhile, groupby

VARIABLE_SECTION_START = 'Pos. = '
VARIABLE_NAME_FIELD = 'Variable = '
VARIABLE_LABEL_FIELD = 'Variable label = '
VALUE_FIELD = 'Value = '
VALUE_LABEL_FIELD = 'Label = '

Variable = namedtuple('Variable', ['id', 'name', 'label', 'values'])


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
    for variable in filter(_variable_has_values, variables):
        lines.append('')
        lines.append('')
        lines.append('class {}Values(Enum):'.format(_convert_name(variable.name)))
        for value, label in variable.values.items():
            lines.append("    {} = '{}'".format(_convert_name(label.upper()), value))
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


def _convert_name(name):
    return name.upper().replace(' ', '_')
