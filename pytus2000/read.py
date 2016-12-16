import pandas as pd

from .datadicts import diary


def read_diary_file(path_to_file):
    return pd.read_csv(
        path_to_file,
        delimiter='\t',
        converters=_column_name_to_type_mapping(diary),
        low_memory=False # some columns seem to have mixed types
    )


def _column_name_to_type_mapping(module):
    mapping = {}
    for member in module.Variable:
        try:
            module.__dict__[member.name]
            mapping[member.name] = _enum_converter(module.__dict__[member.name])
        except KeyError:
            pass # nothing to do; there is no enum
    return mapping


def _enum_converter(enumcls):
    def enum_converter(value):
        if value == ' ':
            return None
        else:
            try:
                value = enumcls(value)
            except ValueError as ve:
                print(ve)
                return None
            else:
                return value
    return enum_converter
