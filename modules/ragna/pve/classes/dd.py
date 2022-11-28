from .player import PVEPlayer

class DD(PVEPlayer):
    def __init__(self, username, session):
        super().__init__(username, session)

        self.role = 'dd'

    def choose_button(self, buttons):
        pass