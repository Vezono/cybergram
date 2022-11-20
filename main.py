from pyrogram import Client, filters
from pyrogram.handlers import *

from src.logger import Logger
from src.ftl import FTL
from src import get_registry

app = Logger()
client = Client("tear", api_id=app.config['api_id'], api_hash=app.config['api_hash'])
ftl = FTL(get_registry(app.config))


def check_if_command(f, c, u):
    if not ftl.id:
        ftl.id = client.get_me().id

    if not u.text:
        return False
    
    if not u.text.startswith('.'):
        return False

    if not u.from_user.id == ftl.id:
        return False
    return True
    

command_filter = filters.create(check_if_command, "userbot_command")


@client.on_message(command_filter)
async def hello(c, m):
    await ftl.process_command(c, m)


@client.on_message()
async def hello(c, m):
    await ftl.process_listener(c, m)

client.add_handler(MessageHandler(app.handler))


client.run()
