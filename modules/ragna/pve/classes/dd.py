from .player import PVEPlayer

class DD(PVEPlayer):
    def __init__(self, username, session):
        super().__init__(username, session, 'дд')
