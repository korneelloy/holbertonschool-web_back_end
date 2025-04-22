#!/usr/bin/env python3
"""
multiple coroutines at the same time with async
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n
    argv:   n : int
            max_delay : int

    You will spawn wait_random n times with the specified max_delay.

    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency.

    """

    tasks = []
    delays = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
