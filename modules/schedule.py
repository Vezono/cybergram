from pyrogram import Client
from pyrogram import types

from src.BaseCommand import BaseCommand


class ScheduleCommand(BaseCommand):
    def __init__(self):
        super().__init__('schedule')

    async def execute(self, c: Client, m: types.Message):
        await m.edit(f'```{c.user.schedule}```')

commands = [ScheduleCommand]
listeners = []