#!/usr/bin/env python3
"""Module"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns the 10 numbers from the previous task"""
    return [i async for i in async_generator()]
