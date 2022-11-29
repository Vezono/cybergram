from src.BaseCommand import BaseCommand

import os
import sys
import git 
import pip

class RebootCommand(BaseCommand):
    def __init__(self):
        super().__init__('reboot')

    async def execute(self, c, m):
        g = git.cmd.Git('.')
        g.pull()
        pip.main(['install', '-r', 'requirements.txt'])
        os.execv(sys.executable, ['python'] + sys.argv)

commands = [RebootCommand]
listeners = []