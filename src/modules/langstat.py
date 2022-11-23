from pyrogram import types, Client

from src.BaseListener import BaseListener
from src.BaseCommand import BaseCommand

from langdetect import detect
import flag

codes = {
    'af': 'ZA',
    'agq': 'CM',
    'ak': 'GH',
    'am': 'ET',
    'ar': 'AE',
    'as': 'IN',
    'asa': 'TZ',
    'az': 'AZ',
    'bas': 'CM',
    'be': 'BY',
    'bem': 'ZM',
    'bez': 'IT',
    'bg': 'BG',
    'bm': 'ML',
    'bn': 'BD',
    'bo': 'CN',
    'br': 'FR',
    'brx': 'IN',
    'bs': 'BA',
    'ca': 'ES',
    'cgg': 'UG',
    'chr': 'US',
    'cs': 'CZ',
    'cy': 'GB',
    'da': 'DK',
    'dav': 'KE',
    'de': 'DE',
    'dje': 'NE',
    'dua': 'CM',
    'dyo': 'SN',
    'ebu': 'KE',
    'ee': 'GH',
    'en': 'GB',
    'el': 'GR',
    'es': 'ES',
    'et': 'EE',
    'eu': 'ES',
    'ewo': 'CM',
    'fa': 'IR',
    'fil': 'PH',
    'fr': 'FR',
    'ga': 'IE',
    'gl': 'ES',
    'gsw': 'CH',
    'gu': 'IN',
    'guz': 'KE',
    'gv': 'GB',
    'ha': 'NG',
    'haw': 'US',
    'he': 'IL',
    'hi': 'IN',
    'ff': 'CN',
    'fi': 'FI',
    'fo': 'FO',
    'hr': 'HR',
    'hu': 'HU',
    'hy': 'AM',
    'id': 'ID',
    'ig': 'NG',
    'ii': 'CN',
    'is': 'IS',
    'it': 'IT',
    'ja': 'JP',
    'jmc': 'TZ',
    'ka': 'GE',
    'kab': 'DZ',
    'ki': 'KE',
    'kam': 'KE',
    'mer': 'KE',
    'kde': 'TZ',
    'kea': 'CV',
    'khq': 'ML',
    'kk': 'KZ',
    'kl': 'GL',
    'kln': 'KE',
    'km': 'KH',
    'kn': 'IN',
    'ko': 'KR',
    'kok': 'IN',
    'ksb': 'TZ',
    'ksf': 'CM',
    'kw': 'GB',
    'lag': 'TZ',
    'lg': 'UG',
    'ln': 'CG',
    'lt': 'LT',
    'lu': 'CD',
    'lv': 'LV',
    'luo': 'KE',
    'luy': 'KE',
    'mas': 'TZ',
    'mfe': 'MU',
    'mg': 'MG',
    'mgh': 'MZ',
    'ml': 'IN',
    'mk': 'MK',
    'mr': 'IN',
    'ms': 'MY',
    'mt': 'MT',
    'mua': 'CM',
    'my': 'MM',
    'naq': 'NA',
    'nb': 'NO',
    'nd': 'ZW',
    'ne': 'NP',
    'nl': 'NL',
    'nmg': 'CM',
    'nn': 'NO',
    'nus': 'SD',
    'nyn': 'UG',
    'om': 'ET',
    'or': 'IN',
    'pa': 'PK',
    'pl': 'PL',
    'ps': 'AF',
    'pt': 'PT',
    'rm': 'CH',
    'rn': 'BI',
    'ro': 'RO',
    'ru': 'RU',
    'rw': 'RW',
    'rof': 'TZ',
    'rwk': 'TZ',
    'saq': 'KE',
    'sbp': 'TZ',
    'seh': 'MZ',
    'ses': 'ML',
    'sg': 'CF',
    'shi': 'MA',
    'si': 'LK',
    'sk': 'SK',
    'sl': 'SI',
    'sn': 'ZW',
    'so': 'SO',
    'sq': 'AL',
    'sr': 'RS',
    'sv': 'SE',
    'sw': 'TZ',
    'swc': 'CD',
    'ta': 'IN',
    'te': 'IN',
    'teo': 'UG',
    'th': 'TH',
    'ti': 'ER',
    'to': 'TO',
    'tr': 'TR',
    'twq': 'NE',
    'tzm': 'MA',
    'uk': 'UA',
    'ur': 'PK',
    'uz': 'UZ',
    'vai': 'LR',
    'vi': 'VN',
    'vun': 'TZ',
    'xog': 'UG',
    'yav': 'CM',
    'yo': 'NG',
    'zh': 'CN',
    'zu': 'ZA'
  }


class LangStatCommand(BaseCommand):
    def __init__(self):
        super().__init__('langstat')

    async def execute(self, c: Client, m: types.Message):
        await m.edit(self.render())

    def load_resources(self, client):
        self.client = client

    def detect_flag(self, lang):
        return flag.flag(codes[lang])

    def render(self):
        stats = self.client.user.storage.load_json('langstat.json')
        percentages = {}
        overall_count = sum([stats[lang] for lang in stats])
        for lang in stats:
            percentage = str(stats[lang]/overall_count*100).split('.')
            percentage = float(f'{percentage[0]}.{percentage[1][:1]}')
            percentages.update({
                lang: percentage
            })


        percentages = dict(sorted(percentages.items(),key= lambda x:x[1], reverse = True))
        tts = 'Статистика за мовами:\n'

        tiny_percentage = 0
        for lang in percentages:
            if percentages[lang] >= 1:
                continue
            tiny_percentage += percentages[lang]
        
        for lang in percentages:
            if percentages[lang] <= 1:
                continue
            tts += f'{self.detect_flag(lang)} - {percentages[lang]}%'+'\n'
        tts += f'🏴 - {tiny_percentage}%'
        return tts

class LangStatListener(BaseListener):

    def __init__(self):
        super().__init__()

    def detect_flag(self, lang):
        return flag.flag(codes[lang])

    async def execute(self, c: Client, m: types.Message):
        if not m.from_user or not m.text or m.forward_date:
            return
        if m.from_user.id != c.id:
            return

        stats = c.user.storage.load_json('langstat.json')

        lang = detect(m.text)
        flag_emoji = self.detect_flag(lang)

        if not lang in stats:
            stats.update({lang: 0})

        stats.update({
            lang: stats[lang]+len(m.text)
        })

        c.user.storage.write_json('langstat.json', stats)

commands = [LangStatCommand]
listeners = [LangStatListener]