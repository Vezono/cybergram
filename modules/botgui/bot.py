from telebot import TeleBot, types
from threading import Thread
from modules import modules_list
from src.core.Cybergram import cybergram
from .pages import init

class BotGui:
    def __init__(self, token):
        self.token: str = token
        self.bot: TeleBot = TeleBot(token)

        self.initialize_handlers()

    @property
    def username(self) -> int:
        return self.bot.get_me().username

    def stop(self):
        self.bot.stop_bot()

    def validator(self, m):
        return m.from_user.id in cybergram.user_ids

    def initialize_handlers(self):
        init(self, self.bot)

    def run(self):
        self.thread = Thread(target=self.bot.infinity_polling)
        self.thread.start()