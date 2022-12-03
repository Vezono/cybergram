from .player import PVEPlayer

class Heal(PVEPlayer):
    def __init__(self, username, session):
        super().__init__(username, session, 'хил')