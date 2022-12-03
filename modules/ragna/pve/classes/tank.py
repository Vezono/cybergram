from .player import PVEPlayer

class Tank(PVEPlayer):
    def __init__(self, username, session):
        super().__init__(username, session, 'танк')
        