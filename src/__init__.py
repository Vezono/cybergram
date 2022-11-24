from src.BaseCommand import BaseCommand
from src.BaseListener import BaseListener

from src.core import Registry
from modules import load_modules
import tomli

with open("accounts.toml", mode="rb") as fp:
    settings = tomli.load(fp)

def get_registry(storage) -> Registry:
    registry = Registry()
    for module in load_modules():
        commands, listeners, name = module

        if 'enabled' in settings[storage.name]:
            if name not in settings[storage.name]['enabled']:
                print(f'[Registry]: {storage.name} skipped {name}')
                continue

        if 'disabled' in settings[storage.name]:
            if name in settings[storage.name]['disabled']:
                print(f'[Registry]: {storage.name} skipped {name}')
                continue
            
        for command in commands:
            registry.register_command(command())
        for listener in listeners:
            registry.register_listener(listener())
        print(f'[Registry]: {storage.name} has loaded {name}')
    return registry
