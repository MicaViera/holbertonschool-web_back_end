#!/usr/bin/env python3
"""Method named get_page that takes two integer arguments page
and page_size."""
from typing import Tuple
import csv
import math
from typing import List


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
        """Method that returns a page."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pages = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pages[0]:pages[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that takes the same arguments (and defaults) as get_page
        and returns a dictionary."""
        all_Data = self.get_page(page, page_size)
        dataset = len(self.dataset())
        total_pages = int(dataset / page_size)
        next_page = 0
        prev_page = 0

        if page + 1 <= total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page - 1 >= 1:
            prev_page = page - 1
        else:
            prev_page = None

        Dictionary = {
            "page_size": page_size,
            "page": page,
            "all_Data": all_Data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return Dictionary


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns a tuple."""
    total_size = page * page_size
    initial_size = total_size - page_size
    return (initial_size, total_size)
