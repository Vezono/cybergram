from requests import get

def get_from_simple(sl, tl, text):
    url = f'https://simplytranslate.org/api/translate?engine=google&text={text}&from={sl}&to={tl}'
    r = get(url)
    return r.json()['translated-text']

def translate_text(from_lang, to_lang, text):
    if not from_lang:
        from_lang = 'auto'
    return get_from_simple(from_lang, to_lang, text)

def parse_translate_command(text):
    text = text[2:]
    if len(text) == 2:
        return None, text
    else:
        from_lang = text.split('2', 1)[0]
        to_lang = text.split('2', 1)[1]
        return from_lang, to_lang

def get_text(m):
    if m.caption:
        return m.caption
    else:
        return m.text
