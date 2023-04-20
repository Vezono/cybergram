from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src.core.Cybergram import cybergram


class VAInfoCommand(BaseCommand):
    def __init__(self):
        super().__init__('vainfo')

    async def execute(self, c: Client, m: types.Message = None):
        for user in cybergram.users:
            if not ('vegan' in user.registry.modules):
                continue
            vegan = user.registry.modules.get('vegan')
            for command in vegan.commands:
                if command.text == 'vinfo':
                    break
            result = await command.execute(user.client)
            await c.send_message(m.chat.id, result)

