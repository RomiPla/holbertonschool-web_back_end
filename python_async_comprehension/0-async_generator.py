#!/usr/bin/env python3
"""Module"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Function o create ten floats"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
