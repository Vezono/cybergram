from src.BaseCommand import BaseCommand

import os
import sys
from src.utils.update import update

class RebootCommand(BaseCommand):
    def __init__(self):
        super().__init__('reboot')

    async def execute(self, c, m):
        await m.edit('Reboot initiated.')
        os.execv(sys.executable, ['python'] + sys.argv)
