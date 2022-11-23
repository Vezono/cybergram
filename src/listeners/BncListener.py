from pyrogram import types, Client

from src.BaseListener import BaseListener
from src.utils.bnc_solver import BncSolver

class BNCListener(BaseListener):
    def __init__(self):
        super().__init__()

    def basic_checks(self, m, c):
        if not m.from_user or not m.text:
            return
        if not c.user.storage.resources.get('bncsolving'):
            c.user.storage.resources['bncsolving'] = {}
        return (m.from_user.id == 586541228)

    async def execute(self, c: Client, m: types.Message):
        if not self.basic_checks(m, c):
            return
        bnc = c.user.storage.resources['bncsolving']
        if not bnc.get(m.chat.id):
            return
        if 'Тип числа: HEX' in m.text:
            bnc[m.chat.id] = None
            return
        if m.text.startswith('Число загадано!'):
            await m.reply(bnc[m.chat.id].possible_nums_list[0])
        if m.text.startswith('Длина числа:'):
            answers = m.text.split('\n')[4:]
            if not answers:
                await m.reply(bnc[m.chat.id].possible_nums_list[0])
                return
            for answer in answers:
                number = int(answer.split(':')[0])
                bulls = int(answer.split(' ')[1][:1])
                cows = int(answer.split(' ')[1][:1])

                if number in bnc[m.chat.id].attempts:
                    continue
                bnc[m.chat.id].attempts.append(number)

                await m.reply(bnc[m.chat.id].guess(bulls, cows, number))
        if ', попыток: ' in m.text:
            m.text = m.text.replace('Уже проверяли! ', '')
            number = int(m.text.split(':')[0])
            bulls = int(m.text.split(' ')[1][:1])
            cows = int(m.text.split(' ')[2][:1])

            if number in bnc[m.chat.id].attempts:
                return
            bnc[m.chat.id].attempts.append(number)

            await m.reply(bnc[m.chat.id].guess(bulls, cows, number))
        if m.text.startswith('Игра "Быки и коровы" в этом чате досрочно завершена! Ответ:') or 'выиграл за' in m.text:
            bnc[m.chat.id] = None
            return
