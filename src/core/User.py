from pyrogram import Client, filters
from pyrogram.handlers import *

import schedule
from threading import Thread
import asyncio
import time

from src.core import Storage, Processor
from src import get_registry

class User:
    def __init__(self, name):
        self.name = name

        self.storage = Storage(name)
        self.client = Client(self.storage.path, self.storage.api_id, self.storage.api_hash)
        self.client.user = self

        self.registry = get_registry(self.storage.config)
        self.registry.load_resources(self.client)
        self.registry.inject_client(self.client)
        
        self.processor = Processor(self.registry)

        self.initialize_handlers()
        self.initialize_client()

    def initialize_client(self):
        self.run()

    def initialize_handlers(self):
        @self.client.on_message(filters.create(self.check_if_command, "userbot_command"))
        async def command_hub(c: Client, m):
            await self.processor.process_command(c, m)


        @self.client.on_message()
        async def listener_hub(c, m):
            await self.processor.process_listener(c, m)

    def run(self):
        self.client.start()

    def check_if_command(self, c, u):
        if not u.text:
            return False
        
        if not u.from_user:
            return False

        if not u.from_user.id == c.id:
            return False

        if not u.text.startswith('.'):
            return False
        return True