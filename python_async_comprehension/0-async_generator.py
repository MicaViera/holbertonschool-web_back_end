#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments."""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function that loops 10 times asynchronously."""
    for index in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
