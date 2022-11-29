import git
import pip

def update():
    g = git.cmd.Git('.')
    g.pull()
    pip.main(['install', '-r', 'requirements.txt'])
    pip.main(['install', '-r', 'modules/requirements.txt'])
    pip.main(['install', '-r', 'modules/*/requirements.txt'])