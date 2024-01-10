#!/usr/bin/env python3
"""Annotate the below function's parameters and return values with the
appropriate types."""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that return the lenght of lst."""
    for index in lst:
        return len(index)
