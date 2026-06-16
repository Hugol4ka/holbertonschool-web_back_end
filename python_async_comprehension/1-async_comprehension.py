#!/usr/bin/env python3
"""
Ce module contient une coroutine qui va prendre
des nombres random.
"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires en utilisant une compréhension
    asynchrone sur async_generator, puis retourne ces 10 nombres.
    """
    return [i async for i in async_generator()]
