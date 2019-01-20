from responses.preprocess import *

commands = {
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

    'но я же': {
        'attachment': 'photo-171283257_456239043'
    },

    'гачи': {
        'random': [
            {'attachment': 'photo-171283257_456239047'},
            {'attachment': 'photo-171283257_456239048'}
        ]
    }
}

commands_regexp = {
    '(?i)(?<![а-яa-z0-9])в\s?пи[зс]ду(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239019'
    },

    '(?i)(?<![а-яa-z0-9])кошкоде[вф]+(очка|ка)(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239025'
    },

    '(?i)^\s*\)\s*$': {
        'attachment': 'photo-171283257_456239034'
    },

    '\){3,}': {
        'random': [
            {'message': '%braces_message%. ВАУ!'},
            {'message': '%braces_message%. Ничего себе!'},
            {'message': '%braces_message%. Вы гений!'},
            {'message': '%braces_message%. Вы лучший!'}
        ],

        'preprocess': process_braces
    },

    '\({3,}': {
        'random': [
            {'message': '%sad_braces_message%. Грустно...'},
            {'message': '%sad_braces_message%. Депрессия сковала тебя.'},
            {'message': '%sad_braces_message%. Разве всё так плохо?'},
            {'message': '%sad_braces_message%. Я заварю чай и принесу плед.'}
        ],

        'preprocess': process_sad_braces
    },

    '(?i)(?<![а-яa-z0-9])дед(а|у|ом|е|ы|ов|ам|ах|ами)?(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239036'
    },

    '(?i)(?<![а-яa-z0-9])я\s+(пидорас|пидарас|ивтшник|педик|пидор|гей|танкист)(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239038'
    },

    '(?i)(?<![а-яa-z0-9])(си|си\+\+|цпп|c|c\+\+)\s+(говн|дерьм)(о|ище)(?![а-яa-z0-9])': {
        'message': 'КАЛ ТВОЙ ГОВНО'
    },

    '(?i)(?<![а-яa-z0-9])(лол)?[кk][eе][кk](ус|лол)?(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239039'
    },

    '(?i)^\s*\:3\s*$': {
        'attachment': 'photo-171283257_456239040'
    },

    '(?i)(?<![а-яa-z0-9])о+го+(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239041'
    },

    '(?i)(?<![а-яa-z0-9])сложн[оа]+(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239044'
    },

    '(?i)(?<![а-яa-z0-9])[хг]+м+(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239045'
    },

    '(?i)^\s*ща\s*$': {
        'attachment': 'photo-171283257_456239023'
    },

    '(?i)(?<![а-яa-z0-9])класс?[еи]ка(?![а-яa-z0-9])': {
        'attachment': 'photo-171283257_456239046'
    },
}
