from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src import decorators

class VeganBattleCommand(BaseCommand):
    def __init__(self):
        super().__init__('vbattle')

    @decorators.silent
    @decorators.with_arguments(2)
    async def execute(self, c: Client, m: types.Message):
        skills = m.text.split(' ', 2)[-2:]
        c.user.storage.update_config({'vegan_skills': skills})

