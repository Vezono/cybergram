from pyrogram import types, Client

from src.BaseListener import BaseListener
from src.commands.vegan_command import q_start


class StartVeganListener(BaseListener):

    def __init__(self):
        super().__init__()

    async def execute(self, c: Client, m: types.Message):
        if m.text == "🔋Энергия полностью восстановлена, вы готовы к сражению!" and m.chat.id == 5505670334:
            await q_start(c)
            await c.send_message("me", "vegan started")
