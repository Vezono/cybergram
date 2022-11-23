from asyncio import sleep

from pyrogram import Client
from pyrogram import types
from pyrogram.enums import UserStatus

from src.BaseCommand import BaseCommand


class DoebCommand(BaseCommand):
    def __init__(self):
        super().__init__('doeb')

    async def execute(self, c: Client, m: types.Message):
        c.is_doeb_running = True
        chat_id = m.chat.id
        while c.is_doeb_running:
            users = await c.get_users([chat_id])
            await sleep(1)
            if users[0].status == UserStatus.ONLINE:
                await c.send_message(chat_id, "ответь")
                await sleep(10)

