from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from time import sleep


class VeganInfoCommand(BaseCommand):
    def __init__(self):
        super().__init__('vinfo')

    async def execute(self, c: Client, m: types.Message = None):
        config = c.user.storage.config
        await c.send_message('@Veganochatwars_bot', '🏅Профиль')
        await m.edit('Loading profile data...') if m else None
        sleep(3)

        tts = f'{config.get("vegan_name")}:\n\n'
        tts += f"💰{config.get('vegan_g')} 👝{config.get('vegan_p')} 🔥{config.get('vegan_e')} 🔋{config.get('vegan_n')}\n"
        tts += f"🗺Farm: {'✅' if config.get('vegan_farm') else '❌'}\n"
        tts += f'🎯Target: {config.get("vegan_target")}\n'
        tts += f'💣Battle items: {", ".join(config.get("vegan_items"))}\n'
        tts += f'💉Battle skills: {", ".join(config.get("vegan_skills"))}\n'

        await m.edit(tts) if m else None
        return tts

