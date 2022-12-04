import random

from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand

class DickCommand(BaseCommand):
    text = 'dick'

    async def execute(self, c: Client, m: types.Message):
        size = random.randint(1, 34)
        user = m.from_user
        if m.reply_to_message:
            user = m.reply_to_message.from_user
        await m.delete()
        await c.send_message(m.chat.id, f'Размер члена {user.first_name} - {size} см')

commands = [DickCommand]
listeners = []