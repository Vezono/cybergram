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
        schedule.every().day.at("07:58", "Europe/Moscow").do(get_normal_from_async, self.send, c)
        schedule.every().day.at("15:58", "Europe/Moscow").do(get_normal_from_async, self.send, c)
        schedule.every().day.at("23:58", "Europe/Moscow").do(get_normal_from_async, self.send, c)
        schedule.every().day.at("08:03", "Europe/Moscow").do(get_normal_from_async, self.send_after, c)
        schedule.every().day.at("16:03", "Europe/Moscow").do(get_normal_from_async, self.send_after, c)
        schedule.every().day.at("00:03", "Europe/Moscow").do(get_normal_from_async, self.send_after, c)

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        target = m.text.replace(".plan ", "")
        if target not in variants:
            await c.send_message("me", f"options are: {' '.join(variants.keys())}")
            return
        self.last_target = target

    async def send(self, c: Client):
        await c.send_message(5505670334, variants[self.last_target])
        await c.send_message(5505670334, "/off_goodsleep")
        await c.send_message(5505670334, "/use_bicepc")
        self.last_target = "def"

    async def send_after(self, c: Client):
        await c.send_message(5505670334, "/off_bicepc")
        await c.send_message(5505670334, "/use_goodsleep")
