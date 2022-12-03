from .storage import storage

def for_leader(func):
    async def wrapper(self, c: Client, m: types.Message):
        if c.id != storage.config['leader']:
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper