from src.BaseCommand import BaseCommand

import os
import sys

class RebootCommand(BaseCommand):
    text = 'reboot'

    async def execute(self, c, m):
        await m.edit('Reboot initiated.')
        os.execv(sys.executable, ['python'] + sys.argv)


class ExitCommand(BaseCommand):
    text = 'exit'

    async def execute(self, c, m):
        await m.edit('Halting!')
        os.kill(os.getpid(), 9)

