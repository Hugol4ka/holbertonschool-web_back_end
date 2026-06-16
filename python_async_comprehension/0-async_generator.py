#!/usr/bin/env python3
"""
Ce module contient une coroutine qui génère des nombres
aléatoires de manière asynchrone.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Boucle 10 fois, attend 1 seconde asynchrone à chaque itération,
    puis produit un nombre aléatoire (float) entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
