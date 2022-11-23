from pyrogram import Client, filters
from pyrogram.handlers import *

import datetime as dt
import scheduler
from threading import Thread
import asyncio
import time

from src.core import Storage, Processor
from src import get_registry

class User:
    def __init__(self, name):
        self.name = name

        self.schedule = scheduler.Scheduler(tzinfo=dt.timezone.utc)

        self.storage = Storage(name)
        self.client = Client(self.storage.path, self.storage.api_id, self.storage.api_hash)
        self.client.user = self

        self.registry = get_registry(self.storage)
        self.registry.load_resources(self.client)
        self.registry.inject_client(self.client)
        
        self.processor = Processor(self.registry)

        self.inject_id()
        self.initialize_sceduler()
        self.initialize_handlers()
        self.initialize_client()

    def inject_id(self):
        with self.client as client:
            self.client.id = client.get_me().id

    def initialize_sceduler(self):
        Thread(target=self.run_schedule).start()

    def initialize_client(self):
        self.run()

    def initialize_handlers(self):
        @self.client.on_message(filters.create(self.check_if_command, "userbot_command"))
        async def command_hub(c: Client, m):
            await self.processor.process_command(c, m)


        @self.client.on_message()
        async def listener_hub(c, m):
            await self.processor.process_listener(c, m)

    def run_schedule(self):
        while True:
            self.schedule.exec_jobs()
            time.sleep(1)

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