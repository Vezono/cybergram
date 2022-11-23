from pyrogram import Client
from pyrogram import types
from src.BaseCommand import BaseCommand

class BootModule(BaseCommand):
    def __init__(self):
        self.text = None
        pass

    async def execute(self, c: Client, m: types.Message):
        pass

    def load_resources(self, client):
        self.client = client
        self.on_start()

    def on_start(self):
        with self.client as client:
            client.id = client.get_me().id
            print(f'[Boot]: {client.user.name} started')

commands = [BootModule]
listeners = []