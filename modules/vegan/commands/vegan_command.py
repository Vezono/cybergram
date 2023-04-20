from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src.utils.periodic import Periodic


async def farm_message(c):
    f = c.user.storage.config.get('farm_message')
    if not f:
        f = await c.send_message(5505670334, '🗺Квесты')
        f = f.id+1
        config = c.user.storage.config
        config.update({'farm_message': f})
        c.user.storage.write_json('config.json', config)
    return f


async def quest(c: Client):
    try:
        if not c.user.storage.config.get('vegan_farm'):
            return
        await c.request_callback_answer(
            chat_id=5505670334,
            message_id = await farm_message(c),
            callback_data="quest_select?castle_protect",
            timeout=1
        )
    except Exception:
        pass


async def q_start(c):
    c.vegan_task = Periodic(quest, 185, c)
    await c.vegan_task.start()


class VeganCommand(BaseCommand):

    task = None

    def __init__(self):
        super().__init__('vegan')

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        c.user.storage.update_config({'vegan_farm': True})
        await q_start(c)

