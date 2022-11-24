from pyrogram import types, Client

from src.BaseListener import BaseListener
from .vegan_command import q_start
import src.decorators as decorators

class StartVeganListener(BaseListener):

    def __init__(self):
        super().__init__()

    @decorators.is_text
    @decorators.from_user
    @decorators.for_id(5505670334)
    async def execute(self, c: Client, m: types.Message):
        if m.text == "🔋Энергия полностью восстановлена, вы готовы к сражению!":
            await q_start(c)
            await c.send_message("me", "vegan started")
