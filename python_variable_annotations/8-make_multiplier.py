#!/usr/bin/env python3
""" module returning callable function with multiplier"""
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function
    argv:   multiplier : float
    returns lambda function multiplying any float"""
    return lambda x: x * multiplier
