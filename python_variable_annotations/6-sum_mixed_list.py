#!/usr/bin/env python3
""" module returning sum of list of ints and floats"""


def sum_mixed_list(mxd_lst: list[float | float]) -> float:
    """type-annotated function
    argv: mxd_lst : list of floats or ints
    returns  sum as a float."""

    result: float = 0
    for i in mxd_lst:
        result += i
    return result
