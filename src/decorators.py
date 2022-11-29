from pyrogram import types, Client

def with_arguments(count):
    def decorator(func):
        async def wrapper(self, c: Client, m: types.Message):
            if m.count(' ') < count:
                return lambda c, m: 1
            await func(self, c, m)
        return wrapper
    return decorator

def for_me(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.from_user:
            return lambda c, m: 1
        if c.id != m.from_user.id:
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper

def for_id(user_id):
    def decorator(func):
        async def wrapper(self, c: Client, m: types.Message):
            if not m.from_user:
                return lambda c, m: 1
            if user_id != m.from_user.id:
                return lambda c, m: 1
            await func(self, c, m)
        return wrapper
    return decorator

def for_ids(user_ids: list):
    def decorator(func):
        async def wrapper(self, c: Client, m: types.Message):
            if not m.from_user:
                return lambda c, m: 1
            if m.from_user.id not in user_ids:
                return lambda c, m: 1
            await func(self, c, m)
        return wrapper
    return decorator

def is_replying(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.reply_to_message:
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper

def is_chat(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.chat:
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper

def is_text(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.text:
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper

@is_chat
def is_private(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.chat.type == 'private':
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper

@is_chat
def is_group(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.chat:
            return lambda c, m: 1
        await func(self, c, m)
    return wrapper

def silent(func):
    async def wrapper(self, c: Client, m: types.Message):
        await m.delete()
        await func(self, c, m)
    return wrapper