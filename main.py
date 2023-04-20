from src.utils.update import update
from src.core.Cybergram import cybergram

update()

try:
    cybergram.run()
except KeyboardInterrupt:
    print('Lol')