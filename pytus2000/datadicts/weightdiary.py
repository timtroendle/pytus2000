"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""
from enum import Enum

from pytus2000.datadicts import OrderedEnum, VariableEnum


class Variable(VariableEnum):
    SN1 = (1, "point number")
    SN2 = (2, "address number")
    SN3 = (3, "Person number")
    WTDT_GR = (4, "Weight for people keeping at least one diary - for grossing to UK population aged 8yrs or more")
    WTDT_UG = (5, "Weight for people keeping at least one diary - ungrossed")
