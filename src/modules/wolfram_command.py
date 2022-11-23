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
        req = m.text.replace(".w ", "")
        await m.edit(f'Request: {req}\nAnswer: Loading...')
        res = self.wclient.query(req)
        text = ""
        for pod in res.results:
            text += pod.text + "\n"
        if text != "":
            await m.edit(f'Request: {req}\nAnswer: Loading...')
        else:
            await m.edit(f'Request: {req}\nAnswer: Nothing found!')

commands = [WolframCommand]
listeners = []
