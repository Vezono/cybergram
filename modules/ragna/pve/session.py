from ..constants import roles, pve_classes
from ..storage import storage

class Session:
    def __init__(self, chat_id):
        self.chat_id = chat_id

        self.boss_hp = 0
        self.minions = 0

        self.players = {}
        self.roles = {_: 0 for _ in roles.values()}
        self.warsong = {_: 0 for _ in storage.config['warsong'].split()}

        self.fixed = False

    @property
    def usernames(self):
        return[self.players[player].username for player in self.players]

    def join(self, c):
        if str(c.id) in storage.config['roles']:
            role = storage.config['roles'][str(c.id)]
        else:
            role = min(self.roles, key=self.roles.get)
        if c.id not in self.players:
            self.roles[role] += 1
            self.players.update({c.id: pve_classes[role](c.username, self)})
        else:
            role = self.players[c.id].role
        return role

    def get_warsong(self):
        song = min(self.warsong, key=self.warsong.get)
        self.warsong[song] += 1
        return song