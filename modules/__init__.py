from pkgutil import iter_modules
from importlib import import_module


def get_module(name: str):
    path = f"modules.{name}"
    module = import_module(f"modules.{name}")
    try:
        return module.commands, module.listeners, name
    except:
        print(f'[ModLoader]: {name} is written incorrectly. Nothing imported from there.')
        return [], [], name

def load_modules():
    for _, name, _ in iter_modules(["modules"]):
        yield get_module(name)

def modules_list():
    for _, name, _ in iter_modules(["modules"]):
        yield name