#!/usr/bin/env python3
"""
coroutine without arguments that loops 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Use the random module.
"""

import random
import asyncio


async def async_generator():
    """asynchronous generator of 10 random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
