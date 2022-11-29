import git
import pip
import os

def update():
    g = git.cmd.Git('./')
    print(g.pull())
    return
    pip.main(['install', '-r', 'requirements.txt'])
    pip.main(['install', '-r', 'modules/requirements.txt'])
    modules = [f.path for f in os.scandir('modules') if f.is_dir()]
    for module in modules:
        pip.main(['install', '-r', f'{module}/requirements.txt'])

update()