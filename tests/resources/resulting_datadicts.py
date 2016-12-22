"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""
from enum import Enum

from pytus2000.datadicts import OrderedEnum, VariableEnum


class Variable(VariableEnum):
    V1 = (1, "variable label 1")
    ATV2 = (2, "variable label 2")
    V3 = (3, "variable label 3")
    V4 = (4, "variable label 4")
    V5 = (5, "variable label 5")
    V6 = (6, "variable label 6")


class V3(OrderedEnum):
    LABEL1 = '0'
    LABEL2 = '1'
    LABEL3 = '2'
    MISSING1 = '99'


class V4(OrderedEnum):
    LABEL = '1.1'
    ATSOME_LABEL = '2.2'
    N1SOME_OTHER_LABEL = '2.3'
    ATSOME_LABEL2 = '2.4'
    MISSING1 = '-1'
    MISSING2 = '-9'


V5 = V3
