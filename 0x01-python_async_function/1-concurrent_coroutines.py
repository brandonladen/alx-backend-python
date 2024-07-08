#!/usr/bin/env python3
''''
Multiple coroutines at the same time
'''


import asyncio
from typing import List
from random import uniform


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''returns a list'''
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    sorted_delays = sorted(delays)
    return sorted_delays
