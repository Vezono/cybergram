from .utils.translate import translate_text, parse_translate_command, get_text
from src.BaseListener import BaseListener
from src import decorators

class TranslateToCommand(BaseListener):

    @decorators.is_text
    async def execute(self, c, m):
        if not m.text.startswith('.t'):
            return
        text = ''
        command = ''
        if m.reply_to_message:
            text = get_text(m.reply_to_message)
            command = m.text
        else:
            text = m.text.split(' ', 1)[1]
            command = m.text.split(' ', 1)[0]

        if not text:
            return

        from_lang, to_lang = parse_translate_command(command)
        translation = translate_text(from_lang, to_lang, text)
        await m.edit(translation)