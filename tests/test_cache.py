"""Tests of the caching mechanism.

These tests are slightly weird. It is difficult to test the caching mechanism without testing
internals. The way this is done here is the following:

The caching mechanism is based on ids. That is, each function and the dataframe it returns have
an id. In the following tests, that mechanism is overwritten by two functions which have distinct
return values but the same id. That way it can always be understood whether a return value is
taken from the function or from cache.
"""
from pathlib import Path
import os

import pandas as pd
from pandas.util.testing import assert_series_equal
import pytest

import pytus2000 as tus
from pytus2000 import cache

CACHE_ID = 'some-cache-id'
DATA = pd.Series([1, 2, 3])
OTHER_DATA = pd.Series([10, 20, 30])


@pytest.fixture
def function_returning_data():
    def some_func():
        return DATA
    return cache.cached(CACHE_ID)(some_func)


@pytest.fixture()
def function_returning_other_data():
    def some_func():
        return OTHER_DATA
    return cache.cached(CACHE_ID)(some_func)


def test_writes_cache(tmpdir, function_returning_data):
    tus.set_cache_location(str(tmpdir))
    data = function_returning_data()
    assert (Path(str(tmpdir)) / cache._CACHE_ROOT_PATH / CACHE_ID).exists()


def test_returns_data_when_writing_to_cache(tmpdir, function_returning_data):
    tus.set_cache_location(str(tmpdir))
    data = function_returning_data()
    assert_series_equal(data, DATA)


def test_does_not_write_to_cache_if_switched_off(tmpdir, function_returning_data):
    tus.set_cache_location(str(tmpdir))
    tus.set_cache_location(None)
    data = function_returning_data()
    assert not (Path(str(tmpdir)) / cache._CACHE_ROOT_PATH / CACHE_ID).exists()


def test_returns_data_when_switched_off(tmpdir, function_returning_data):
    tus.set_cache_location(str(tmpdir))
    tus.set_cache_location(None)
    data = function_returning_data()
    assert_series_equal(data, DATA)


def test_reads_from_cache_if_valid(tmpdir, function_returning_data, function_returning_other_data):
    tus.set_cache_location(str(tmpdir))
    data_first = function_returning_data()

    data_second = function_returning_other_data() # should return OTHER_DATA, but is read from cache
    assert_series_equal(data_second, DATA)


def test_does_not_read_from_cache_if_pytus_version_changes(tmpdir, function_returning_data,
                                                           function_returning_other_data):
    tus.cache.__version__ = '0.0.0.test'
    tus.set_cache_location(str(tmpdir))
    data_first = function_returning_data()

    tus.cache.__version__ = '0.0.1.test'
    data_second = function_returning_other_data()
    assert_series_equal(data_second, OTHER_DATA)


def test_does_not_read_from_cache_if_pandas_version_changes(tmpdir, function_returning_data,
                                                            function_returning_other_data):
    pd.__version__ = '0.0.0.test'
    tus.set_cache_location(str(tmpdir))
    data_first = function_returning_data()

    pd.__version__ = '0.0.1.test'
    data_second = function_returning_other_data()
    assert_series_equal(data_second, OTHER_DATA)


def test_allows_wiping_cache(tmpdir, function_returning_data):
    tus.set_cache_location(str(tmpdir))
    data = function_returning_data()

    tus.wipe_cache()
    assert not (Path(str(tmpdir)) / cache._CACHE_ROOT_PATH / CACHE_ID).exists()
