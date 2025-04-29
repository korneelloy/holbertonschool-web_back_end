#!/usr/bin/env python3

"""
returning list based upon start page and page sze
"""

import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function returning index of elements based upon start page and page size
    argv:
        int : page
        int: page_size
    Returns: tuple of start and end index
    """
    return (((page - 1) * page_size), (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returning list based upon start page and page size
        """
        assert isinstance(page, int), "page must be an integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert (page > 0), "page must be greater than 0"
        assert (page_size > 0), "page_size must be greater than 0"
        index = index_range(page, page_size)
        data = self.dataset()
        list = []
        for row in data[index[0]:index[1]]:
            if row is not None:
                list.append(row)
        return list

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[str, Union[int, None, List[List]]]:
        """
        returning dict with info based upon start page and page size
        """
        data = self.get_page(page, page_size)
        data_size = len(data)

        total_data = self.dataset()
        total_data_size = len(total_data)
        total_pages = math.ceil(total_data_size / page_size)
        next_page = None
        if data_size != 0:
            next_page = page + 1
        prev_page = None
        if page != 1:
            prev_page = page - 1

        dict = {
            'page_size': data_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return dict
