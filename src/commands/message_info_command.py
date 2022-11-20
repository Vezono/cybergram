from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand


class MessageInfoCommand(BaseCommand):
    def __init__(self):
        super().__init__('info')

    async def execute(self, c: Client, m: types.Message):
        await c.send_message("me", f"{m.reply_to_message.id} {m.reply_to_message.reply_markup}")
