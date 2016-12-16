from collections import namedtuple
from itertools import dropwhile, groupby

VARIABLE_SECTION_START = 'Pos. = '
VARIABLE_NAME_FIELD = 'Variable = '
VARIABLE_LABEL_FIELD = 'Variable label = '
VALUE_FIELD = 'Value = '
VALUE_LABEL_FIELD = 'Label = '

Variable = namedtuple('Variable', ['id', 'name', 'label', 'values'])


class DataDictionaryParser():

    def __init__(self, path_to_file):
        with path_to_file.open('r') as txt_file:
            lines = txt_file.readlines()
        lines = filter(lambda line: line is not '\n', lines)
        lines = dropwhile(lambda line: not line.startswith(VARIABLE_SECTION_START), lines)
        lines = (line.rstrip('\n') for line in lines)
        variable_sections = self._variable_section_generator(lines)
        self.variables = [self._parse_variable(variable_section)
                          for variable_section in variable_sections]
        self.number_variables = len(list(variable_sections))

    @classmethod
    def _parse_variable(cls, variable_section):
        variable_section = list(variable_section)
        position, name, label = variable_section[0].split('\t')
        value_lines = filter(lambda line: line.startswith(VALUE_FIELD), variable_section)
        return Variable(
            id=int(position.split(VARIABLE_SECTION_START)[1]),
            name=name.split(VARIABLE_NAME_FIELD)[1],
            label=label.split(VARIABLE_LABEL_FIELD)[1],
            values=cls._parse_variable_values(value_lines)
        )

    @staticmethod
    def _parse_variable_values(value_lines):
        values = {
            value.split(VALUE_FIELD)[1]: label.split(VALUE_LABEL_FIELD)[1]
            for value, label in (line.split('\t') for line in value_lines)
        }
        return values if len(values) > 0 else None

    @staticmethod
    def _variable_section_generator(lines):
        variable_section = []
        for line in lines:
            if line.startswith(VARIABLE_SECTION_START) and len(variable_section) > 0:
                yield variable_section
                variable_section = []
            variable_section.append(line)
        yield variable_section
