#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Function that waits for a random delay n times."""
    delays = []
    for idx in range(n):
        delays.append(task_wait_random(max_delay))
    result = await asyncio.gather(*delays)
    return sorted(result)
