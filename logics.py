import re

commands = {
    'впизду': {
        'attachment': 'photo-171283257_456239019'
    },

    'F': {
        'attachment': 'photo-171283257_456239020'
    },

    'справедливо': {
        'sticker_id': '163'
    },

    'можно ненадо': {
        'attachment': 'photo-171283257_456239021'     
    },

    'ебать спасибо нахуй': {
        'attachment': 'photo-171283257_456239022'
    }
}


def process_command(command):
    for k, v in commands.items():
        l_command = r'\s+'.join(re.split(r'\s+', k))
        if (re.search('(?i)(?<![а-яa-z])' + l_command + '(?![а-яa-z])', command) is not None):
            return v
