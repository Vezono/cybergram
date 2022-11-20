from pyrogram import Client, filters
from pyrogram.handlers import *

from src.logger import Logger
from src.processor import Processor
from src import get_registry

from startup import app, client
processor = Processor(get_registry(app.config))
client.stop()

def check_if_command(f, c, u):
    if not u.text:
        return False
    
    if not u.text.startswith('.'):
        return False

    if not u.from_user.id == processor.id:
        return False
    return True
    


@client.on_message(filters.create(check_if_command, "userbot_command"))
async def hello(c: Client, m):
    await processor.process_command(c, m)


@client.on_message()
async def listener_hub(c, m):
    await processor.process_listener(c, m)

client.run()
