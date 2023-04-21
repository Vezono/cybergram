from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src.core.Cybergram import cybergram


class VAVeganCommand(BaseCommand):
    def __init__(self):
        super().__init__('vavegan')

    async def execute(self, c: Client, m: types.Message = None):
        for user in cybergram.users:
            if not ('vegan' in user.registry.modules):
                continue
            vegan = user.registry.modules.get('vegan')
            for command in vegan.commands:
                if command.text == 'vegan':
                    break
            try:
                await c.send_message(m.chat.id, f'{user.name} acknowledged.')
            except:
                print(f'[vegan] {user.name} can\'t execute .vegan command.')

