#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Function that waits for a random delay n times."""
    delays = []
    for idx in range(n):
        delays.append(wait_random(max_delay))
    result = await asyncio.gather(*delays)
    return sorted(result)
