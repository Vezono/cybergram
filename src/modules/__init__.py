from pkgutil import iter_modules
from importlib import import_module
import tomli

with open("tic_tac_toe.toml", mode="rb") as fp:
     config = tomli.load(fp)


def load_modules(package: str = "src/modules"):
    """
    Iterates over a package and returns classes of the same name with their modules
        Keyword arguments:
        package -- relative path to the package (default "src/commands/common")
    """
    for _, name, _ in iter_modules([package]):
        path = f"{package.replace('/','.')}.{name}"
        module = import_module(f"{package.replace('/','.')}.{name}")
        try:
            yield module.commands, module.listeners, name
        except:
            print(f'[ModLoader]: {name} is written incorrectly. Nothing imported from there.')
            yield [], [], name
