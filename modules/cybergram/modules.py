from pyrogram import Client
from pyrogram import types

from src.BaseCommand import BaseCommand

from src import decorators
from modules import modules_list



class ModulesCommand(BaseCommand):
    def __init__(self):
        super().__init__('modules')

    async def execute(self, c: Client, m: types.Message):
        tts = "**Modules: **\n"
        for module in modules_list():
            tts += f'{"🟢" if module in c.user.registry.modules else "🔴"}`{module}`\n'
        await m.edit(tts)

class ModuleCommand(BaseCommand):
    def __init__(self):
        super().__init__('module')

    @decorators.with_arguments(1)
    async def execute(self, c: Client, m: types.Message):
        name = m.text.split(' ', 1)[1]
        if name not in c.user.registry.modules:
            await m.edit(f'```[ModLoader]: "{name}" module is not loaded.```')
        module = c.user.registry.modules[name]
        tts = f'**Module {name}: **\n\nCommands:\n'
        for command in module.texts:
            tts += f'•`.{command}`\n'
        tts += '\nListeners:\n'
        for listener in module.listeners:
            lname = f'{str(type(listener))}'.replace("<", "").replace(">", "").split('.')[-1].replace("'", "")
            tts += f'•`{lname}`\n'
        await m.edit(tts)

class UnloadModuleCommand(BaseCommand):
    def __init__(self):
        super().__init__('unload')

    @decorators.with_arguments(1)
    async def execute(self, c: Client, m: types.Message):
        name = m.text.split(' ', 1)[1]
        if name not in c.user.registry.modules:
            await m.edit(f'```[ModLoader]: "{name}" module is not loaded.```')
        c.user.registry.unload_module(name)
        await m.edit(f'```[ModLoader]: 🔴"{name}" unloaded.```')

class LoadModuleCommand(BaseCommand):
    def __init__(self):
        super().__init__('load')

    @decorators.with_arguments(1)
    async def execute(self, c: Client, m: types.Message):
        name = m.text.split(' ', 1)[1]
        if name not in modules_list():
            await m.edit(f'[ModLoader]: "{name}" module is not installed.')
        if name in c.user.registry.modules:
            await m.edit(f'[ModLoader]: "{name}" module is already loaded.')
        c.user.registry.load_module(name)
        await m.edit(f'[ModLoader]: 🟢"{name}" loaded.')