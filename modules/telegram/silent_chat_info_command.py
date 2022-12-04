from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand


class SilentChatInfoCommand(BaseCommand):
    text = 'chat'

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        await c.send_message('me', self.format(m))

    def format(self, m):
        tts = 'Chat info:\n'
        tts += f'ID: {m.chat.id}\n'
        tts += f'Title: {m.chat.title}\n'
        return tts