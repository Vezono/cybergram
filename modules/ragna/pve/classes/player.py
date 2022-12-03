from ...constants import *
from ...utils import *
from .. import priorities

class PVEPlayer:
    def __init__(self, username, session, role):
        self.hp = 100
        self.username = username

        self.role = role
        self.subrole = ''

        self.states = set()
        self.priority = priorities.NORMAL

        self.session = session

    def choose(self, buttons):
        choices = self.parse_buttons(buttons)
        for choice in self.priority:
            if not choices[choice]:
                continue
            return choices[choice][0]

    def parse_buttons(self, buttons: list):
        choices = {_: [] for _ in self.priority}
        for button in buttons:
            btext, rsp = button.lower(), button.rfind(' ')
            p1, p2 = btext[:rsp], btext[rsp + 1:]
            
            if p1 in dl_p1 and p2 in dl_p2:
                choices['role'].append(button)
            elif p1 in tl_p1 and p2 in tl_p2:
                choices['role'].append(button)
            elif p1 in hl_p1 and is_username(p2):
                choices['role'].append(button)
            elif btext in concentrate_list:
                choices['concentrate'].append(button)
            elif btext in monk_list:
                choices['subrole'].append(button)
            elif btext in stand_still:
                choices['standstill'].append(button)
            elif p1 in minions_p1 and p2 in minions_p2:
                choices['minions'].append(button)
            elif p1 in deathpunch_list and is_username(p2):
                choices['deathsave'].append(button)
            elif button in flame_list:
                choices['puddle'].append(button)
            elif 'в ответ' in button.lower():
                choices['in_answer'].append(button)
            else:
                choices['jokes'].append(button)
            for misc in hl_misc:
                if misc in btext:
                    choices['role'].append(button)
        return choices

    def parse_turn(self, turn_log: str):
        self.hp = turn_log.split(': ')[1].split('❤️')[0]
        for state in states:
            if state in turn_log:
                self.states.add(states[state])
            elif states[state] in self.states:
                self.states.remove(states[state])
        self.priority = priorities.NORMAL
        if 'otrek' in self.states:
            self.priority = priorities.OTREK