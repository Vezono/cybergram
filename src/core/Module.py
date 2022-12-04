from src import BaseCommand, BaseListener
from typing import List

class Module:
    def __init__(self, name: str, commands: List[BaseCommand], listeners: List[BaseListener]):
        self.name = name
        self.commands = commands
        self.listeners = listeners

        self.install()

    @property
    def texts(self):
        for command in self.commands:
            yield command.text

    def install(self):
        self.commands = list(map(lambda f: f(), self.commands))
        self.listeners = list(map(lambda f: f(), self.listeners))