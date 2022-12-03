from pyrogram import types, Client

no = lambda c, m: 1

def with_arguments(count=1):
    def decorator(func):
        async def wrapper(self, c: Client, m: types.Message):
            if not m.text:
                return no
            if m.text.count(' ') < count:
                return no
            await func(self, c, m)
        return wrapper
    return decorator

def for_me(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.from_user:
            return no
        if c.id != m.from_user.id:
            return no
        await func(self, c, m)
    return wrapper

def for_id(user_id):
    def decorator(func):
        async def wrapper(self, c: Client, m: types.Message):
            if not m.from_user:
                return no
            if user_id != m.from_user.id:
                return no
            await func(self, c, m)
        return wrapper
    return decorator

def for_ids(user_ids: list):
    def decorator(func):
        async def wrapper(self, c: Client, m: types.Message):
            if not m.from_user:
                return no
            if m.from_user.id not in user_ids:
                return no
            await func(self, c, m)
        return wrapper
    return decorator

def is_replying(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.reply_to_message:
            return no
        await func(self, c, m)
    return wrapper

def is_chat(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.chat:
            return no
        await func(self, c, m)
    return wrapper

def is_text(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.text:
            return no
        await func(self, c, m)
    return wrapper

@is_chat
def is_private(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.chat.type == 'private':
            return no
        await func(self, c, m)
    return wrapper

@is_chat
def is_group(func):
    async def wrapper(self, c: Client, m: types.Message):
        if not m.chat:
            return no
        await func(self, c, m)
    return wrapper

def silent(func):
    async def wrapper(self, c: Client, m: types.Message):
        await m.delete()
        await func(self, c, m)
    return wrapper