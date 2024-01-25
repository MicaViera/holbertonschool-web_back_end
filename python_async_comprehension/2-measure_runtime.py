#!/usr/bin/env python3
"""Write a measure_runtime coroutine that will execute async_comprehension four
times in parallel using asyncio.gather."""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Function that measures the total runtime and return it."""
    start_time = time.monotonic()
    task = [async_comprehension() for x in range(4)]
    await asyncio.gather(*task)
    return (time.monotonic() - start_time)
