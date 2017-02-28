import pandas as pd
import numpy as np

from .datadicts import diary, individual
from .cache import cached
from .transform import transform_diary_data_to_timeseries

_DIARY_DATA_CACHE_ID = 'diary-data'
_DIARY_DATA_TIME_SERIES_CACHE_ID = 'diary-data-time-series'
_INDIVIDUAL_DATA_CACHE_ID = 'individual-data'


@cached(_DIARY_DATA_CACHE_ID)
def read_diary_file(path_to_file):
    """Reads the tab-delimited diary data set.

    Parameters:
        * path_to_file: either a string or a pathlib.Path

    Returns:
        The diary data set as a pandas DataFrame.
    """
    return _read_file(
        module=diary,
        index_columns=4,
        path_to_file=path_to_file
    )


@cached(_INDIVIDUAL_DATA_CACHE_ID)
def read_individual_file(path_to_file):
    """Reads the tab-delimited individual data set.

    Parameters:
        * path_to_file: either a string or a pathlib.Path

    Returns:
        The individual data set as a pandas DataFrame.
    """
    return _read_file(
        module=individual,
        index_columns=3,
        path_to_file=path_to_file
    )


@cached(_DIARY_DATA_TIME_SERIES_CACHE_ID)
def read_diary_file_as_timeseries(path_to_file):
    """Reads the time-varying columns of the tab-delimited diary data set as a timeseries.

    Parameters:
        * path_to_file: either a string or a pathlib.Path

    Returns:
        The time varying columns of the diary data set as a pandas DataFrame time series.
    """
    diary_data = read_diary_file(path_to_file)

    return transform_diary_data_to_timeseries(diary_data)


def _read_file(module, index_columns, path_to_file):
    converter_map = _column_name_to_type_mapping(module)
    data = pd.read_csv(
        path_to_file,
        delimiter='\t',
        converters=converter_map,
        index_col=list(range(index_columns)),
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
                print(f"{ve}. Will be replaced by np.nan.")
                return np.nan
            else:
                return value
    return enum_converter
