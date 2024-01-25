#!/usr/bin/env python3
"""Create a measure_time function with integers n and max_delay."""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Function  that measures the total execution time for wait_n."""
    total_time = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    return ((time.monotonic() - total_time) / n)
