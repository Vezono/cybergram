from src.core import Storage
storage = Storage('ragna', 'resources')
if not storage.config:
    print('Fresh Ragna install.')
    storage.write_json('config.json', {'leader': 0})
storage.leader = storage.config['leader']
storage.games = {}