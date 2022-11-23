from asyncio import sleep

from pyrogram import Client
from pyrogram import types
from pyrogram.enums import UserStatus

from src.BaseCommand import BaseCommand


class DoebCancelCommand(BaseCommand):
    def __init__(self):
        super().__init__('nodoeb')

    async def execute(self, c: Client, m: types.Message):
        c.is_doeb_running = False

