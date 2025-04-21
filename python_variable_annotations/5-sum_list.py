#!/usr/bin/env python3
""" module returning sum of list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function
    argv: list of floats
    returns  sum as a float."""

    result: float = 0
    for i in input_list:
        result += i
    return result
