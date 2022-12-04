from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
import src.decorators as decorators

class SilentUserInfoCommand(BaseCommand):
    text = 'user'

    @decorators.silent
    async def execute(self, c: Client, m: types.Message):
        user = m.from_user
        if m.reply_to_message:
            user = m.reply_to_message.from_user
        await c.send_message('me', self.format(user))

    def format(self, user):
        tts = 'User info:\n'
        tts += f'ID: {user.id}\n'
        tts += f'Username {user.username}\n'
        tts += f'First Name: {user.first_name}\n'
        tts += f'Online status: {user.status.value}'
        return tts
