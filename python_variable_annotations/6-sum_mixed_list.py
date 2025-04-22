#!/usr/bin/env python3
""" module returning sum of list of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated function
    argv: mxd_lst : list of floats or ints
    returns  sum as a float."""

    result: float = 0
    for i in mxd_lst:
        result += i
    return result
