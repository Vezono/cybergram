from pyrogram import types, Client

from src.BaseListener import BaseListener
import src.decorators as decorators


class ProfileVeganListener(BaseListener):

    @decorators.is_text
    @decorators.for_id(5505670334)
    async def execute(self, c: Client, m: types.Message):
        if not "Битва четырех замков через" in m.text:
            return

        g = m.text.split('💰')[1].split(' ')[0]
        p = m.text.split('👝')[1].split(' ')[0].split('\n')[0]
        e = m.text.split('🔥')[1].split(' ')[2].split('\n')[0]
        n = m.text.split('🔋')[1].split(' ')[1].split('\n')[0]
        name = m.text.split('\n')[2]
        c.user.storage.update_config({'vegan_g': g, 'vegan_p': p, 'vegan_e': e, 'vegan_n': n, 'vegan_name': name})
