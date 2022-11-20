from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand

from startup import client

class PingCommand(BaseCommand):
    def __init__(self):
        super().__init__('no_command')

        self.on_start()

    async def execute(self, c: Client, m: types.Message):
        await m.reply('Working.')

    def on_start(self):
        self.get_normal_from_async(client.send_message, ['me', 'Модуль инициализирован.'])
        # do stuff
