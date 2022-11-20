from pyrogram import Client
from pyrogram import types


class BaseListener:
    def __init__(self):
        pass

    def validate(self):
        pass

    async def execute(self, c: Client, m: types.Message):
        await c.send_message('me', 'Basic listener executed. Check your code btw')

    def load_resources(self, *args, **kwargs):
        pass
