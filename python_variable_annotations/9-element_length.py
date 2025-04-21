#!/usr/bin/env python3
""" module returning callable function with multiplier"""
from collections.abc import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[tuple[int]]:
    """type-annotated function
    argv:   multiplier : float
    returns lambda function multiplying any float"""
    return [(i, len(i)) for i in lst]
