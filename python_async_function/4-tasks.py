#!/usr/bin/env python3
"""
Ce module contient la coroutine task_wait_n qui gère plusieurs
tâches asyncio de manière concurrente.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawne task_wait_random n fois avec le max_delay spécifié.
    Renvoie la liste de tous les délais (floats) dans l'ordre croissant
    (ordre de complétion).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
