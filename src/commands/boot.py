from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand

from startup import client

class BootModule(BaseCommand):
    def __init__(self):
        super().__init__('no_command')

    async def execute(self, c: Client, m: types.Message):
        pass

    def on_start(self):
        with client:
            client.send_message('me', 'Boot started.')
            client.id = client.get_me().id
            print('ID Injected.')


