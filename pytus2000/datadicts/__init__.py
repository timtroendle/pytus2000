"""This subpackage contains all data dictionaries."""
# The Python source code gets auto-generated and this package is intentially empty.
from enum import Enum


class VariableEnum(Enum):
    """Contains all variables in a datadict.

    Parameters:
        * position: the position in the datadict (int)
        * label: the string describing the variable
    """

    def __init__(self, position, label):
        self.position = position
        self.label = label
