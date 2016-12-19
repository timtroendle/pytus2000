import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--runwithdataset",
        action="store_true",
        help="run tests involving the data set"
    )
