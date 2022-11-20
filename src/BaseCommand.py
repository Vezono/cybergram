from pyrogram import Client
from pyrogram import types
import asyncio

class BaseCommand:
    def __init__(self, text="basic"):
        self.text = text
        self.on_start()

    def on_start(self):
        print(f'Module {self.text} loaded.')

    async def notice(self, c: Client):
        await c.send_message('me', f'{self.text} usage notice')

    async def execute(self, c: Client, m: types.Message):
        await self.notice(c)
        await c.send_message('me', 'Basic command executed. Check your code btw')

    def load_resources(self, *args, **kwargs):
        pass

    def get_normal_from_async(function, *args, **kwargs):
        asyncio.run(function(*args, **kwargs))


