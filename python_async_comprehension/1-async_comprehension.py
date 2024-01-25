#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments."""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Function that loops 10 times asynchronously."""
    random_numbers = []
    async for index in async_generator():
        random_numbers.append(index)
    return random_numbers
