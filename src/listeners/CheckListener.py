from pyrogram import types, Client

from src.BaseListener import BaseListener


class CheckListener(BaseListener):

    def __init__(self):
        super().__init__()

    async def execute(self, c: Client, m: types.Message):
        if m.text == "check_listener":
            await c.send_message("me", "check ok")
