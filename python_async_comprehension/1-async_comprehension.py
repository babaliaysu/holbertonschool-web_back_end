#!/usr/bin/env python3
"""
Bu modul əvvəlki tapşırıqdan asinxron generatoru import edir və
asinxron list comprehension vasitəsilə məlumatları toplayır.
"""
from typing import List

# async_generator funksiyasını import edirik
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asinxron generatoru işə salır və asinxron comprehension
    vasitəsilə 10 təsadüfi ədədi siyahı halında geri qaytarır.
    """
    return [i async for i in async_generator()]
