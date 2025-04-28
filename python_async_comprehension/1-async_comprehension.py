#!/usr/bin/env python3
"""
coroutine that takes no arguments, that
will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """asynchronous generator of 10 random numbers"""
    result = []
    async for i in async_generator():
        result.append(i)
    return (result)
