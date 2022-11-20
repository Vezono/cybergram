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

    def get_normal_from_async(self, function, *args, **kwargs):
        try:
            asyncio.run(function(*args, **kwargs))
        except:
            pass
        #asyncio.get_event_loop().create_task(function(*args, **kwargs))


