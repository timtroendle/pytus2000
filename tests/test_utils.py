from datetime import time

import pytest

from pytus2000.utils import time_mapper


@pytest.mark.parametrize("input,expected", [
    ("001", time(4, 0)),
    ("007", time(5, 0)),
    ("144", time(3, 50)),
    (1, time(4, 0)),
    (7, time(5, 0)),
    (144, time(3, 50))
])
def test_time_mapper(input, expected):
    assert time_mapper(input) == expected
