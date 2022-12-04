from src.BaseCommand import BaseCommand
from src.BaseListener import BaseListener

from .session import Session
from ..storage import storage
from ..constants import *
from src import decorators
from ..utils import *
from .. import rdecorators

from pyrogram import Client

class RagnaGoCommand(BaseCommand):
    text = 'ragnago'

    async def execute(self, c, m):
        storage.games.update({m.chat.id: Session(m.chat.id)})
        await m.reply('рагна вставай')

class PvePlayerListListener(BaseListener):
    @decorators.for_id(ragna_id)
    @decorators.is_text
    async def execute(self, c, m):
        if m.chat.id not in storage.games:
            return
        players = parse_list(m)
        if not players:
            return
        if c.id != storage.config['leader']:
            return
        game = storage.games[m.chat.id]
        ready = True
        for username in game.usernames:
            if username not in players:
                ready = False
                break
        if ready:
            await m.reply('Мы готовы')
        else:
            if game.fixed:
                return
            await m.reply('^join')
            game.fixed = True

class PveWinListener(BaseListener):
    @decorators.for_id(ragna_id)
    @rdecorators.for_leader
    @decorators.is_text
    async def execute(self, c, m):
        if m.chat.id not in storage.games:
            return
        if not m.text.startswith('🎉 Хорошая битва 🎉'):
            return
        storage.games.update({m.chat.id: Session(m.chat.id)})
        await m.reply('рагна вставай')

class ChatJoinListener(BaseListener):
    @decorators.for_id(storage.config['leader'])
    @decorators.with_arguments(1)
    async def execute(self, c: Client, m):
        if m.text.split(' ')[0] != '^join':
            return
        await c.join_chat(m.text.split()[1])

class PveJoinListener(BaseListener):
    @decorators.for_id(storage.config['leader'])
    @decorators.is_text
    async def execute(self, c, m):
        if m.chat.id not in storage.games:
            return
        if m.text != '^join':
            return
        role = storage.games[m.chat.id].join(c)
        await m.reply('я тест')
        await m.reply(f'я {role}')

class DoWarsongListener(BaseListener):
    @decorators.for_id(storage.config['leader'])
    @decorators.is_text
    async def execute(self, c, m):
        if m.chat.id not in storage.games:
            return
        if m.text != '^warsong':
            return
        await m.reply(storage.games[m.chat.id].get_warsong())

class PveStartListener(BaseListener):
    @decorators.for_id(ragna_id)
    @decorators.is_text
    async def execute(self, c, m):
        if m.chat.id not in storage.games:
            return
        if m.text != 'КТО ОСМЕЛИЛСЯ ПРИЗВАТЬ МЕНЯ? 👿':
            return
        role = storage.games[m.chat.id].join(c)
        await m.reply(f'я {role}')

class PveButtonListener(BaseListener):
    @decorators.for_id(ragna_id)
    @decorators.is_text
    async def execute(self, c, m):
        if m.chat.id not in storage.games:
            return
        if parse_list(m):
            return
        if not m.mentioned or not m.reply_markup:
            return
        try:
            m.reply_markup.keyboard
        except:
            return
        if not '❤️' in m.text:
            return
        player = storage.games[m.chat.id].players[c.id]
        player.parse_turn(m.text)
        buttons = get_buttons(m)
        if len(buttons) == 5:
            return
        await m.reply(player.choose(buttons))