import pandas as pd
import numpy as np

from .datadicts import diary


def read_diary_file(path_to_file):
    """Reads in the tab-delimited diary data set.

    Parameters:
        * path_to_file: either a string or a pathlib.Path

    Returns:
        The diary data set as a pandas DataFrame.
    """
    converter_map = _column_name_to_type_mapping(diary)
    data = pd.read_csv(
        path_to_file,
        delimiter='\t',
        converters=converter_map,
        index_col=[0, 1, 2, 3],
        low_memory=False # some columns have mixed types
    )
    category_map = {}
    for col in filter(_columns_name_in_dataframe(data), converter_map.keys()):
        category_map[col] = 'category'
    data = data.astype(category_map, copy=False)
    return data


def _columns_name_in_dataframe(dataframe):
    def _columns_name_in_dataframe(column_name):
        return column_name in dataframe
    return _columns_name_in_dataframe


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
            return np.nan
        else:
            try:
                value = enumcls(value)
            except ValueError as ve:
                print("{}. Will be replaced by np.nan.".format(ve))
                return np.nan
            else:
                return value
    return enum_converter
