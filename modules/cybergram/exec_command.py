from src.BaseCommand import BaseCommand
from src import decorators
import traceback

class ExecCommand(BaseCommand):
    def __init__(self):
        super().__init__('reboot')

    @decorators.with_arguments()
    async def execute(self, c, m):
        code = m.text.split(' ')[1:]
        tts = f'Code:\n{code}'
        try:
            tts += f'\n\nResult: {exec(code)}'
        except:
            tts += f'\n\nError: {traceback.format_exc()}'
        m.edit(tts)
