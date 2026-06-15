#!/usr/bin/env python3
"""
Ce module contient une routine permettant d'exécuter plusieurs
coroutines en même temps (en concurrence).
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """
    Exécute wait_random 'n' fois avec le 'max_delay' spécifié.

    Renvoie la liste de tous les délais dans l'ordre croissant,
    générée naturellement grâce à la concurrence.
    """
    taches = [wait_random(max_delay) for _ in range(n)]
    delais = []
    for tache in asyncio.as_completed(taches):
        delai = await tache
        delais.append(delai)
    return delais
