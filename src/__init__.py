
from src.core import Registry
from src.modules import load_modules

def get_registry(storage) -> Registry:
    registry = Registry()
    for module in load_modules():
        commands, listeners, name = module
        for command in commands:
            registry.register_command(command())
        for listener in listeners:
            registry.register_listener(listener())
        print(f'[Registry]: {storage.name} has loaded {name}')
    return registry
