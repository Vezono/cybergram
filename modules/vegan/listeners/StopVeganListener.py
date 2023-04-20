from pyrogram import types, Client

from src.BaseListener import BaseListener
import src.decorators as decorators


class StopVeganListener(BaseListener):

    @decorators.is_text
    @decorators.for_id(5505670334)
    async def execute(self, c: Client, m: types.Message):
        if m.text == "Недостаточно выносливости!":
            await c.vegan_task.stop()
            c.user.storage.update_config({'vegan_farm': False})
