"""This subpackage contains all data dictionaries."""
# The Python source code gets auto-generated and this package is intentially empty.
from enum import Enum


class OrderedEnum(Enum):
    """An Enum whose members are ordered by their value."""

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class VariableEnum(OrderedEnum):
    """Contains all variables in a datadict.

    Parameters:
        * position: the position in the datadict (int)
        * label: the string describing the variable
    """

    def __init__(self, position, label):
        self.position = position
        self.label = label
