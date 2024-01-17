#!/usr/bin/env python3
"""Function named index_range that takes two integer arguments page
and page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns a tuple."""
    total_size = page * page_size
    initial_size = total_size - page_size
    return (initial_size, total_size)
