#!/usr/bin/env python3
"""
Measure the runtime
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function measering execution time of wait_n(n, max_delay)
    argv:
        n: int
        max_delay: int

    returns total_time / n : float.

    Use the time module to measure an approximate elapsed time.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return ((end_time - start_time) / n)
