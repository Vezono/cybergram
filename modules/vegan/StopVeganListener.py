from pyrogram import types, Client

from src.BaseListener import BaseListener
import src.decorators as decorators
from .vegan_command import VeganCommand


class StopVeganListener(BaseListener):

    def __init__(self):
        super().__init__()

    @decorators.is_text
    @decorators.for_id(5505670334)
    async def execute(self, c: Client, m: types.Message):
        if m.text == "Недостаточно выносливости!":
            await c.vegan_task.stop()
            await c.send_message("me", "vegan ended")
