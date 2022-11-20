import time
from threading import Thread

import schedule
from pyrogram import Client, filters
from pyrogram.handlers import *

from src.logger import Logger
from src.processor import Processor
from src import get_registry

from startup import app, client
registry = get_registry(app.config)
registry.load_resources(client)
processor = Processor(registry)

def check_if_command(f, c, u):
    if not u.text:
        return False
    
    if not u.from_user:
        return False

    if not u.from_user.id == c.id:
        return False

    if not u.text.startswith('.'):
        return False
    return True
    
@client.on_message(filters.create(check_if_command, "userbot_command"))
async def command_hub(c: Client, m):
    await processor.process_command(c, m)


@client.on_message()
async def listener_hub(c, m):
    await processor.process_listener(c, m)

def sched():
    while True:
        schedule.run_pending()
        time.sleep(1)

Thread(target=sched).start()
client.run()
