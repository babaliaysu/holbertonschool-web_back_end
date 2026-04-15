#!/usr/bin/env python3
"""
Bu modulda 10 dəfə dövr edən və hər dəfə 1 saniyə gözləyən
asinxron generator funksiyası yerləşir.
"""
import asyncio
import random


async def async_generator():
    """
    10 dəfə dövr edir, hər dəfə asinxron olaraq 1 saniyə gözləyir
    və 0 ilə 10 arasında təsadüfi bir ədəd qaytarır (yield).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
