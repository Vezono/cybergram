import asyncio


def get_normal_from_async(function, *args, **kwargs):
    asyncio.get_event_loop().create_task(function(*args, **kwargs))
