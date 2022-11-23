import wolframalpha
from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand


class WolframCommand(BaseCommand):
    def __init__(self):
        super().__init__('w')
        self.wclient = None

    async def execute(self, c: Client, m: types.Message):
        if not self.wclient:
            self.wclient = wolframalpha.Client(c.user.storage.config['wolfram'])
        res = self.wclient.query(m.text.replace(".w ", ""))
        text = ""
        for pod in res.results:
            text += pod.text + "\n"
        await m.delete()
        if text != "":
            await c.send_message(m.chat.id, text)

commands = [WolframCommand]
listeners = []
