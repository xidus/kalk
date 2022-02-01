"""
Kalkulator for your sums, substractions and multiplications.

"""

from typing import (
    Union,
    Iterable,
)
import builtins


_sum = builtins.sum


ArgumentType = Union[int, float]
ResultType = Union[int, float]


def sum(*args: Iterable[ArgumentType]) -> ResultType:
    """
    Returnerer summen af de givne argumenter.

    """
    return _sum(args)


def sub(*args: Iterable[ArgumentType]) -> ResultType:
    """
    Returnerer differencen mellem det første argument og de efterfølgende argumenter.

    """
    first, *remainders = args
    return first - sum(*remainders)


def mul(*args: Iterable[ArgumentType]) -> ResultType:
    """
    Returnerer produktet af de givne argumenter.

    """
    product = 1
    for factor in args:
        product *= factor
    return product

