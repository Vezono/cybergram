from pkgutil import iter_modules
from importlib import import_module


def load_modules(package: str = "src/modules"):
    for _, name, _ in iter_modules([package]):
        path = f"{package.replace('/', '.')}.{name}"
        module = import_module(f"{package.replace('/', '.')}.{name}")
        try:
            yield module.commands, module.listeners, name
        except:
            print(f'[ModLoader]: {name} is written incorrectly. Nothing imported from there.')
            yield [], [], name
