import asyncio


def get_normal_from_async(function, *args, **kwargs):
    asyncio.run(function(*args, **kwargs))
