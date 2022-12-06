from telebot import TeleBot, types
from threading import Thread
from modules import modules_list
from src.core.Cybergram import cybergram
from .utils import divide_by_rows

class BotGui:
    def __init__(self, token):
        self.token: str = token
        self.bot = TeleBot(token)

        self.initialize_handlers()

    @property
    def username(self) -> int:
        return self.bot.get_me().username

    def stop(self):
        self.bot.stop_bot()

    def validator(self, m):
        return m.from_user.id in cybergram.user_ids

    def initialize_handlers(self):
        bot = self.bot
        @self.bot.message_handler(commands=['start'], func=self.validator)
        def hi(m):
            self.bot.reply_to(m, 'Greetings.')

        @self.bot.message_handler(commands=['modules'], func=self.validator)
        def hi(m):
            user = cybergram.get_user(m.from_user.id)

            kb = types.InlineKeyboardMarkup()
            buttons = []
            tts = "*Modules: *\n"
            for module in modules_list():
                tts += f'{"🟢" if module in user.registry.modules else "🔴"}`{module}`\n'
                buttons.append(types.InlineKeyboardButton(f'{"🟢" if module in user.registry.modules else "🔴"}{module}\n', callback_data=f"m?{module}"))
            buttons = divide_by_rows(3, buttons)
            for row in buttons:
                kb.add(*row)
            bot.reply_to(m, tts, parse_mode='Markdown', reply_markup=kb)

        @self.bot.callback_query_handler(func=lambda c: c.data.startswith('m?'))
        def m(c):
            user = cybergram.get_user(c.from_user.id)
            print(f'{c.from_user.id} in {cybergram.user_ids}' if not user else 'ok')
            module = c.data.split('?')[1]
            user.registry.switch_module(module)

            kb = types.InlineKeyboardMarkup()
            buttons = []
            tts = "*Modules: *\n"
            for module in modules_list():
                tts += f'{"🟢" if module in user.registry.modules else "🔴"}`{module}`\n'
                buttons.append(types.InlineKeyboardButton(f'{"🟢" if module in user.registry.modules else "🔴"}{module}\n', callback_data=f"m?{module}"))
            buttons = divide_by_rows(3, buttons)
            for row in buttons:
                kb.add(*row)
            bot.edit_message_text(tts, chat_id=c.message.chat.id, message_id=c.message.message_id, parse_mode='Markdown', reply_markup=kb)

    def run(self):
        self.thread = Thread(target=self.bot.infinity_polling)
        self.thread.start()