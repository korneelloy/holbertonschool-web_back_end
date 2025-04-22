#!/usr/bin/env python3
""" module returning callable function with multiplier"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """type-annotated function
    argv:   multiplier : float
    returns lambda function multiplying any float"""
    return [(i, len(i)) for i in lst]
