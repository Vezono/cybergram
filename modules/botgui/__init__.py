from src import BaseCommand, decorators
from .bot import BotGui
from .storage import storage
from traceback import format_exc

class BotGuiCommand(BaseCommand):
    text = "gui"

    @decorators.with_arguments(1)
    async def execute(self, c, m):
        if storage.gui:
            storage.gui.stop()

        token = m.text.split(' ', 1)[1]
        storage.gui = BotGui(token)

        bot_id = 0
        try:
            bot_username = storage.gui.username
        except:
            await m.edit('Wrong token.')
            del storage.gui
            return

        storage.update_config({'token': token})
        storage.gui.run()
        await c.send_message(bot_username, '/start')
        await m.edit('Configuration succsessful.')

    def ready(self):
        if storage.config.get('token'):
            storage.gui = BotGui(storage.config.get('token'))
            storage.gui.run()
        

commands = [BotGuiCommand]
listeners = []