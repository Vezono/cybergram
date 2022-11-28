from .classes.player import PVEPlayer
from ..constants import roles
from ..storage import storage

class Session:
    def __init__(self, chat_id):
        self.chat_id = chat_id

        self.boss_hp = 0
        self.minions = 0

        self.players = {}
        self.roles = {_: 0 for _ in roles.values()}

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
            self.players.update({c.id: PVEPlayer(c.username, self, role)})
        else:
            role = self.players[c.id].role
        return role