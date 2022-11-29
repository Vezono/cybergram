from pyrogram import types, Client

from src.BaseListener import BaseListener
from .vegan_command import q_start
import src.decorators as decorators

class StartVeganListener(BaseListener):

    @decorators.is_text
    @decorators.for_id(5505670334)
    async def execute(self, c: Client, m: types.Message):
        if m.text == "🔋Энергия полностью восстановлена, вы готовы к сражению!":
            await q_start(c)
            await c.send_message("me", "vegan started")
