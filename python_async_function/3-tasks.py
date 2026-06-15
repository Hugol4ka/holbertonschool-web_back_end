#!/usr/bin/env python3
"""
Ce module contient une fonction classique permettant de créer
et de renvoyer une tâche asyncio (Task) à partir d'une coroutine.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Prend un entier max_delay et renvoie une asyncio.Task
    qui exécute la coroutine wait_random en arrière-plan.
    """
    asyncio.create_task(wait_random(max_delay))
    tache = asyncio.create_task(wait_random(max_delay))
    return tache
