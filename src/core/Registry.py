from typing import List
import tomli

from src.BaseCommand import BaseCommand
from src.BaseListener import BaseListener
from src.core import Storage, Module
from modules import load_modules, get_module

class Registry:
    def __init__(self, storage: Storage):
        self.storage = storage

        self.modules = {}
        self.initialize_modules()

    @property
    def listeners(self):
        for module in self.modules.values():
            for listener in module.listeners:
                yield listener

    @property
    def commands(self):
        for module in self.modules.values():
            for command in module.commands:
                yield command

    def get_settings(self):
        with open("accounts.toml", mode="rb") as fp:
            return tomli.load(fp)

    def load_module(self, module: str):
        commands, listeners, name = get_module(module)
        self.modules.update({name: Module(name, commands, listeners)})
        print(f'[Registry]: {self.storage.name} has loaded {name}')
    
    def unload_module(self, module: str):
        del self.modules[module]

    def switch_module(self, module: str):
        if module in self.modules:
            self.unload_module(module)
        else:
            self.load_module(module)

    def initialize_modules(self):
        settings = self.get_settings()
        for module in load_modules():
            commands, listeners, name = module

            if 'enabled' in settings[self.storage.name]:
                if name not in settings[self.storage.name]['enabled']:
                    continue

            if 'disabled' in settings[self.storage.name]:
                if name in settings[self.storage.name]['disabled']:
                    continue

            self.modules.update({name: Module(name, commands, listeners)})
            print(f'[Registry]: {self.storage.name} has loaded {name}')
        return self

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

    def ready(self):
        for i in self.listeners:
            i.ready()
        for i in self.commands:
            i.ready()

    async def execute(self, text, c, m):
        for command in self.commands:
            if command.text == text:
                await command.execute(c, m)

    async def listen(self, c, m):
        for listener in self.listeners:
            await listener.execute(c, m)
