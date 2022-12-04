from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand


class PingCommand(BaseCommand):
    text = 'ping'

    async def execute(self, c: Client, m: types.Message):
        await m.reply('Working.')
