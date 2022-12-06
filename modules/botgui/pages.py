from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import divide_by_rows
from src.core.Cybergram import cybergram
from modules import modules_list

def page(page):
    def check(c):
        if c.data.split('?')[0] != 'p':
            return False
        return c.data.split('?')[1] == page
    return check

def Button(text, page):
    return InlineKeyboardButton(text, callback_data=f'p?{page}')

def edit(c, kb, text):
    m = c.message
    bot.edit_message_text(text, m.chat.id, m.message_id, parse_mode="HTML", reply_markup=kb)

def modules_page(m):
    user = cybergram.get_user(m.from_user.id)
    kb = InlineKeyboardMarkup()
    buttons = []
    tts = "*Modules: *\n"
    for module in modules_list():
        tts += f'{"🟢" if module in user.registry.modules else "🔴"}`{module}`\n'
        buttons.append(InlineKeyboardButton(f'{"🟢" if module in user.registry.modules else "🔴"}{module}\n', callback_data=f"m?{module}"))
    buttons = divide_by_rows(3, buttons)
    for row in buttons:
        kb.add(*row)
    kb.add(Button('◀️Main menu', 'main'))
    return tts, kb

def init(self, bot):
    @bot.message_handler(commands=['start'], func=self.validator)
    def hi(m):
        buttons = [
            Button('🔩Modules', 'modules'),
            Button('📈Statistics', 'stats'),
            Button('🤖Accounts', 'accounts')
        ]
        kb = InlineKeyboardMarkup()
        buttons = divide_by_rows(2, buttons)
        for row in buttons:
            kb.add(*row)
        bot.send_message(m.chat.id, 'Welcome to Cybergram.', reply_markup=kb)

    @bot.callback_query_handler(func=page('modules'))
    def hi(m):
        tts, kb = modules_page(m)
        bot.edit_message_text(tts, chat_id=m.message.chat.id, message_id=m.message.message_id, parse_mode='Markdown', reply_markup=kb)

    @bot.callback_query_handler(func=page('stats'))
    def hi(m):
        user = cybergram.get_user(m.from_user.id)
        tts = '*📈Statistics*:\n'
        tts += f'- `{len(cybergram.users)}` accounts\n'
        tts += f'- `{len(user.registry.modules.keys())}` modules\n'
        tts += f'- `{len(list(user.registry.commands))}` commands\n'
        tts += f'- `{len(list(user.registry.listeners))}` listeners\n'
        kb = InlineKeyboardMarkup([[Button('◀️Main menu', 'main')]])
        
        bot.edit_message_text(tts, chat_id=m.message.chat.id, message_id=m.message.message_id, parse_mode='Markdown', reply_markup=kb)

    @bot.callback_query_handler(func=page('accounts'))
    def hi(m):
        kb = InlineKeyboardMarkup()
        buttons = []
        for user in cybergram.users:
            buttons.append(InlineKeyboardButton(f'{"🟢" if user.active else "🔴"}{user.name}', callback_data=f"u?{user.id}"))
        for row in divide_by_rows(4, buttons):
            kb.add(*row)
        kb.add(Button('◀️Main menu', 'main'))
        bot.edit_message_text('🤖Accounts', chat_id=m.message.chat.id, message_id=m.message.message_id, parse_mode='Markdown', reply_markup=kb)

    @bot.callback_query_handler(func=lambda c: c.data.startswith('m?'))
    def hi(c):
        user = cybergram.get_user(c.from_user.id)
        module = c.data.split('?')[1]
        user.registry.switch_module(module)
        
        tts, kb = modules_page(m)
        bot.edit_message_text('🤖Accounts', chat_id=c.message.chat.id, message_id=c.message.message_id, parse_mode='Markdown', reply_markup=kb)
    
    @bot.callback_query_handler(func=lambda c: c.data.startswith('u?'))
    def hi(c):
        user = cybergram.get_user(int(c.data.split('?')[1]))
        user.active = not user.active
        
        kb = InlineKeyboardMarkup()
        buttons = []
        for user in cybergram.users:
            buttons.append(InlineKeyboardButton(f'{"🟢" if user.active else "🔴"}{user.name}', callback_data=f"u?{user.id}"))
        for row in divide_by_rows(4, buttons):
            kb.add(*row)
        kb.add(Button('◀️Main menu', 'main'))
        bot.edit_message_text('🤖Accounts', chat_id=c.message.chat.id, message_id=c.message.message_id, parse_mode='Markdown', reply_markup=kb)

    @bot.callback_query_handler(func=page('main'))
    def hi(c):
        buttons = [
            Button('🔩Modules', 'modules'),
            Button('📈Statistics', 'stats'),
            Button('🤖Accounts', 'accounts')
        ]
        kb = InlineKeyboardMarkup()
        buttons = divide_by_rows(2, buttons)
        for row in buttons:
            kb.add(*row)
        bot.edit_message_text('Welcome to Cybergram.', chat_id=c.message.chat.id, message_id=c.message.message_id, parse_mode='Markdown', reply_markup=kb)

    @bot.inline_handler(func=self.validator)
    def qe(q):
        user = cybergram.get_user(q.from_user.id)
        results = []
        for module in user.registry.modules.values():
            for command in module.commands:
                text = f".{command.text}" if not q.query else f".{command.text} {q.query}"
                results.append(InlineQueryResultArticle(command.text, f"{module.name} - .{command.text}", InputTextMessageContent(text)))
        bot.answer_inline_query(q.id, results)