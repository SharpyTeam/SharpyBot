import random
import re

commands = {
    'впизду': {
        'attachment': 'photo-171283257_456239019'
    },

    'F': {
        'random': [
            {'attachment': 'photo-171283257_456239020'},
            {'attachment': 'photo-171283257_456239033'}
        ]
    },

    'справедливо': {
        'random': [
            {'sticker_id': '163'},
            {'attachment': 'photo-171283257_456239037'}
        ]
    },

    'можно ненадо': {
        'attachment': 'photo-171283257_456239021'
    },

    'ебать спасибо нахуй': {
        'attachment': 'photo-171283257_456239022'
    },

    'ща': {
        'attachment': 'photo-171283257_456239023'
    },

    'пизда пизда огорчение': {
        'attachment': 'photo-171283257_456239024'
    },

    'капец': {
        'attachment': 'photo-171283257_456239030'
    },

    'глубокий вздох': {
        'attachment': 'photo-171283257_456239028'
    },

    'ебош': {
        'attachment': 'photo-171283257_456239026'
    },

    'ъеъ': {
        'attachment': 'photo-171283257_456239029'
    },

    'доброе утро': {
        'random': [
            {'attachment': 'photo-171283257_456239032'},
            {'attachment': 'photo-171283257_456239031'}
        ]
    },

    'произошел троллинг': {
        'attachment': 'photo-171283257_456239035'
    },

    'справедливость': {
        'attachment': 'photo-171283257_456239037'
    },

    'кек': {
        'attachment': 'photo-171283257_456239039'
    },

    'но я же': {
        'attachment': 'photo-171283257_456239043'
    },
}

commands_regexp = {
    '(?i)(?<![а-яa-z0-9])кошкоде[вф]+(очка|ка)(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239025'
    },

    '^\s*\)\s*$': {
        'attachment': 'photo-171283257_456239034'
    },

    '(?i)(?<![а-яa-z0-9])де(д|да|ду|дом|де)(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239036'
    },

    '(?i)(?<![а-яa-z0-9])я\s+(пидорас|пидарас|ивтшник|педик|пидор|гей)(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239038'
    },

    '(?i)(?<![а-яa-z0-9])(си|си\+\+|цпп|c|c\+\+)\s+(говн|дерьм)(о|ище)(?![а-яa-z0-9])': {
        'message': 'КАЛ ТВОЙ ГОВНО'
    },

    '^\s*\:3\s*$': {
        'attachment': 'photo-171283257_456239040'
    },

    '(?i)(?<![а-яa-z0-9])о+го+(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239041'
    }
}


def process_found_entry(entry):
    if 'random' not in entry:
        return entry
    else:
        return random.choice(entry['random'])


def process_command(command):
    command = command.replace("ё", "е")
    for k, v in commands.items():
        l_command = r'\s+'.join(re.split(r'\s+', k))
        if re.search('(?i)(?<![а-яa-z0-9])' + l_command + '(?![а-яa-z0-9])', command) is not None:
            return process_found_entry(v)

    for k, v in commands_regexp.items():
        if re.search(k, command) is not None:
            return process_found_entry(v)


if __name__ == '__main__':
    print(process_command(input()))
