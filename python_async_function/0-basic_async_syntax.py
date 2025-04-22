#!/usr/bin/env python3
"""
asynchronous wait random
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """"
    asynchronous coroutine "wait_random"
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds
    argv : max_delay (integer, with a default value of 10)
    returns: random delay
    """
    seconds: float = random.uniform(0, max_delay)
    await asyncio.sleep(seconds)
    return seconds
