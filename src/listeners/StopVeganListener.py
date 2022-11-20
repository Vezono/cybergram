from pyrogram import types, Client

from src.BaseListener import BaseListener
from src.commands.vegan_command import VeganCommand


class StopVeganListener(BaseListener):

    def __init__(self):
        super().__init__()

    async def execute(self, c: Client, m: types.Message):
        if m.text == "Недостаточно выносливости!" and m.chat.id == 5505670334:
            await VeganCommand.task.stop()
            await c.send_message("me", "vegan ended")
