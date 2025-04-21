#!/usr/bin/env python3
""" module returning tupple"""
import math


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """type-annotated function
    argv:   k: string
            v: int or float
    returns tuple of k and square of v (float)"""

    return (k, math.pow(v, 2))
