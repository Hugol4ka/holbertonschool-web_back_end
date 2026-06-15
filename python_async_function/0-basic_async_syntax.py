#!/usr/bin/env python3
"""
Ce module contient les fonctions de base pour l'asynchronisme.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un nombre aléatoire de secondes compris entre 0 et max_delay.

    Args:
        max_delay (int): Le délai maximum en secondes.

    Returns:
        float: Le nombre de secondes attendues.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
