from pathlib import Path
import json

import pandas as pd

from .version import __version__

_CACHE_ROOT_PATH = Path('pytus-cache')


def get_cache_location():
    """Returns the directory into which caches are currently written to and from."""
    return _Cache().cache_location


def set_cache_location(cache_location):
    """Sets the directory into which caches are currently written to and from."""
    _Cache().cache_location = cache_location


def wipe_cache():
    """Empties the directory into which caches are currently written to and from."""
    _Cache().wipe()


class cached():
    """Decorator caching return values of functions that always return the same pandas dataframe.

    This is used to cache the time consuming reading of the pytus files for example. It
    is based on an id, i.e. each cached function and the data set it produces has exactly
    one id.
    """

    def __init__(self, cache_id):
        self._cache_id = cache_id

    def __call__(self, f):
        def wrapped_f(*args):
            return _Cache().use_cache_or_call(self._cache_id, f, *args)
        return wrapped_f


class _SingletonType(type):
    """A meta class that creates classes applying the singleton pattern."""

    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(_SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance


class _Cache(metaclass=_SingletonType):

    def __init__(self):
        self._cache_location = None

    @property
    def cache_location(self):
        return self._cache_location

    @cache_location.setter
    def cache_location(self, new_cache_location):
        if new_cache_location is None:
            self._cache_location = None
        else:
            new_cache_location = Path(new_cache_location)
            (new_cache_location / _CACHE_ROOT_PATH).mkdir(parents=True, exist_ok=True)
            self._cache_location = new_cache_location

    def wipe(self):
        root_path = (self._cache_location / _CACHE_ROOT_PATH)
        for path in root_path.rglob('*'):
            path.unlink()
        root_path.rmdir()

    def use_cache_or_call(self, cache_id, read_function, *args):
        if self._cache_location is not None:
            path_to_cache = self._cache_location / _CACHE_ROOT_PATH / cache_id
            if self._valid_cache_exists(cache_id):
                return pd.read_pickle(path_to_cache)
            else:
                path_to_cache.parent.mkdir(parents=True, exist_ok=True)
                path_to_metadata = path_to_cache.with_suffix('.json')
                with path_to_metadata.open('w') as fmetadata:
                    json.dump(self._create_cache_metadata(), fmetadata)
                df = read_function(*args)
                df.to_pickle(path_to_cache)
                return df
        else:
            return read_function(*args)

    def _valid_cache_exists(self, cache_id):
        path_to_cache = self._cache_location / _CACHE_ROOT_PATH / cache_id
        path_to_metadata = path_to_cache.with_suffix('.json')
        if not path_to_cache.exists() or not path_to_metadata.exists():
            return False
        expected_metadata = self._create_cache_metadata()
        with path_to_metadata.open('r') as fmetadata:
            metadata = json.load(fmetadata)
        return expected_metadata == metadata

    @staticmethod
    def _create_cache_metadata():
        return {
            'version.pytus2000': __version__,
            'version.pandas': pd.__version__
        }
