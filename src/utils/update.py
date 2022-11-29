
def update():
    g = git.cmd.Git('.')
    g.pull()
    pip.main(['install', '-r', 'requirements.txt'])