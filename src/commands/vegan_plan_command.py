from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
import schedule

from src.utils.scheduler_for_async import get_normal_from_async

variants = {
    "rat": "🐭Крысиный замок",
    "necro": "🖤Замок некроманта",
    "dark": "👁Замок тьмы",
    "def": "🛡Защита"
}


class VeganPlanCommand(BaseCommand):
    def __init__(self):
        super().__init__('plan')
        self.last_target = "def"

    def load_resources(self, c: Client):
        schedule.every().day.at("07:58").do(get_normal_from_async, self.send, c)
        schedule.every().day.at("15:58").do(get_normal_from_async, self.send, c)
        schedule.every().day.at("23:58").do(get_normal_from_async, self.send, c)

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        target = m.text.replace(".plan ", "")
        if target not in variants:
            await c.send_message("me", f"options are: {' '.join(variants.keys())}")
            return
        self.last_target = target

    async def send(self, c: Client):
        print("ss")
        await c.send_message(5505670334, variants[self.last_target])
        self.last_target = "def"
