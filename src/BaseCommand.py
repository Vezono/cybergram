from pyrogram import Client
from pyrogram import types
import asyncio

class BaseCommand:
    def __init__(self, text=None):
        if text:
            self.text = text
        self.on_start()

    def on_start(self):
        pass

    async def notice(self, c: Client):
        await c.send_message('me', f'{self.text} usage notice')

    async def execute(self, c: Client, m: types.Message):
        await self.notice(c)
        await c.send_message('me', 'Basic command executed.')

    def load_resources(self, *args, **kwargs):
        pass

    def ready(self):
        pass

    def on_stop(self):
        pass


