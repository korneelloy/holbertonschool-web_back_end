#!/usr/bin/env python3

"""
help function for index
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function returning index of elements based upon start page and page size
    argv:
        int : page
        int: page_size
    Returns: tuple of start and end index
    """
    return (((page - 1) * page_size), (page * page_size))
