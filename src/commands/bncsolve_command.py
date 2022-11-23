import random

from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand
from src.utils.bnc_solver import BncSolver

class BNCSolveCommand(BaseCommand):
    def __init__(self):
        super().__init__('bncsolve')

    async def execute(self, c: Client, m: types.Message):
        await m.delete()
        if not c.user.storage.resources.get('bncsolving'):
            c.user.storage.resources['bncsolving'] = {}
        if not m.text.count(' '):
            length = 4
        else:
            length = int(m.text.split(' ', 1)[1])
        c.user.storage.resources['bncsolving'][m.chat.id] = BncSolver(length)
        await m.reply(f'/bnc {length}')