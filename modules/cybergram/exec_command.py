from src.BaseCommand import BaseCommand
from src import decorators
import traceback

class ExecCommand(BaseCommand):
    text = 'exec'

    @decorators.with_arguments()
    async def execute(self, c, m):
        code = m.text.split(' ', 1)[1]
        tts = f'Code:\n{code}'
        try:
            result = exec(code)
            tts += f'\n\nResult: {result}'
        except:
            tts += f'\n\nError: {traceback.format_exc()}'
        await m.edit(tts)

class AExecCommand(BaseCommand):
    text = 'aexec'

    @decorators.with_arguments()
    async def execute(self, c, m):
        code = m.text.split(' ', 1)[1]
        tts = f'Code:\n{code}'
        try:
            result = exec(code)
            tts += f'\n\nResult: {result}'
        except:
            tts += f'\n\nError: {traceback.format_exc()}'
        await m.edit(tts)

class EvalCommand(BaseCommand):
    text = 'eval'

    @decorators.with_arguments()
    async def execute(self, c, m):
        code = m.text.split(' ', 1)[1]
        tts = f'Code:\n{code}'
        try:
            result = eval(code)
            tts += f'\n\nResult: {result}'
        except:
            tts += f'\n\nError: {traceback.format_exc()}'
        await m.edit(tts)

class AEvalCommand(BaseCommand):
    text = 'aeval'

    @decorators.with_arguments()
    async def execute(self, c, m):
        code = m.text.split(' ', 1)[1]
        tts = f'Code:\n{code}'
        try:
            result = await eval(code)
            tts += f'\n\nResult: {result}'
        except:
            tts += f'\n\nError: {traceback.format_exc()}'
        await m.edit(tts)