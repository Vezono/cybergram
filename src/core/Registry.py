from typing import List

from src.BaseCommand import BaseCommand
from src.BaseListener import BaseListener


class Registry:
    def __init__(self):
        self.registry = {}
        self.listeners: List[BaseListener] = []
        self.commands: List[BaseCommand] = []

    def load_resources(self, client):
        for i in self.listeners:
            i.load_resources(client)
        for i in self.commands:
            i.load_resources(client)

    def inject_client(self, client):
        for i in self.listeners:
            i.client = client
        for i in self.commands:
            i.client = client

    def register_command(self, command):
        self.commands.append(command)
        self.registry.update({
            command.text: command
        })

    def register_listener(self, listener):
        self.listeners.append(listener)

    async def execute(self, command, c, m):
        if not self.registry.get(command):
            return
        await self.registry[command].execute(c, m)

    async def listen(self, c, m):
        for listener in self.listeners:
            await listener.execute(c, m)
