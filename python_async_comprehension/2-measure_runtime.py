#!/usr/bin/env python3
"""
Ce module mesure le temps d'exécution de plusieurs coroutines
lancées en parallèle.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps d'exécution total de 4 compréhensions
    asynchrones lancées en parallèle.
    """
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
