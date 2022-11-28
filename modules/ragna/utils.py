def isletter(l: str):
    return (l in '@_ ') or l.isalpha() or l.isdecimal()


def clean_ab(s):
    return ''.join(filter(isletter, s))


def is_username(s):
    if s == 'HEXBOPATb':
        return False
    return len(s) >= 5 and all(s.split('_'))


def get_buttons(m):
    l = []
    for i in m.reply_markup.keyboard:
        l += [clean_ab(j) for j in i]
    return l

def parse_list(m):
    lines = m.text.split('\n')
    if not 'Путин' in lines[-1]:
        return
    if not 'значит' in lines[0] or 'ладно' in lines[0]:
        return
    players = m.text.split('\n\n')[1].split('\n')
    return [player.split(' ')[-1] for player in players]