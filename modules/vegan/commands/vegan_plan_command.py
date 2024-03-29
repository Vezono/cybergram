from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
import src.decorators as decorators

import datetime as dt

from src.utils.scheduler_for_async import get_normal_from_async

tz_moscow = dt.timezone(dt.timedelta(hours=-3))

variants = {
    "rat": "🐭Крысиный замок",
    "necro": "🖤Замок некроманта",
    "dark": "👁Замок тьмы",
    "def": "🛡Защита"
}


class VeganPlanCommand(BaseCommand):
    def __init__(self):
        super().__init__('plan')

    def load_resources(self, c: Client):
        c.user.storage.update_config({'vegan_farm': False})
        c.user.storage.update_config({'vegan_items': []}) if not c.user.storage.config.get('vegan_items') else None
        c.user.storage.update_config({'vegan_skills': []}) if not c.user.storage.config.get('vegan_skills') else None

        schedule = c.user.schedule
        schedule.daily(dt.time(hour=7, minute=58, tzinfo=tz_moscow), lambda: get_normal_from_async(self.send, c))
        schedule.daily(dt.time(hour=15, minute=58, tzinfo=tz_moscow), lambda: get_normal_from_async(self.send, c))
        schedule.daily(dt.time(hour=23, minute=58, tzinfo=tz_moscow), lambda: get_normal_from_async(self.send, c))  

        schedule.daily(dt.time(hour=8, minute=3, tzinfo=tz_moscow), lambda: get_normal_from_async(self.send_after, c))
        schedule.daily(dt.time(hour=16, minute=3, tzinfo=tz_moscow), lambda: get_normal_from_async(self.send_after, c))
        schedule.daily(dt.time(hour=0, minute=3, tzinfo=tz_moscow), lambda: get_normal_from_async(self.send_after, c))        

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        target = m.text.replace(".plan ", "")
        if target not in variants:
            await c.send_message("me", f"options are: {' '.join(variants.keys())}")
            return
        c.user.storage.update_config({'vegan_target': target})

    async def send(self, c: Client):
        await c.send_message(5505670334, variants[c.user.storage.config.get("vegan_target")])
        await c.send_message(5505670334, "/off_goodsleep")
        await c.send_message(5505670334, "/off_greedy")
        skills = c.user.storage.config['vegan_skills']
        items = c.user.storage.config['vegan_items']
        for skill in skills:
            await c.send_message(5505670334, f"/use_{skill}")
        for item in items:
            await c.send_message(5505670334, f"/takeitem_{item}")
        c.user.storage.update_config({'vegan_target': 'def'})

    async def send_after(self, c: Client):
        skills = c.user.storage.config['vegan_skills']
        for skill in skills:
            await c.send_message(5505670334, f"/off_{skill}")
        await c.send_message(5505670334, "/use_greedy")
        await c.send_message(5505670334, "/use_goodsleep")
