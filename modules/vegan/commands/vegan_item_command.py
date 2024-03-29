from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src import decorators

class VeganItemCommand(BaseCommand):
    def __init__(self):
        super().__init__('vitem')

    @decorators.silent
    @decorators.with_arguments(2)
    async def execute(self, c: Client, m: types.Message):
        items = m.text.split(' ')[1:]
        c.user.storage.update_config({'vegan_items': items})

