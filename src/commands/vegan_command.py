from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src.utils.periodic import Periodic


async def quest(c: Client):
    try:
        await c.request_callback_answer(
            chat_id=5505670334,
            message_id=1810007,
            callback_data="quest_select?castle_protect",
            timeout=1
        )
    except Exception:
        pass


async def q_start(c):
    VeganCommand.task = Periodic(quest, 185, c)
    await VeganCommand.task.start()


class VeganCommand(BaseCommand):

    task = None

    def __init__(self):
        super().__init__('vegan')

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        await q_start(c)

