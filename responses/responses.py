import database
from responses.preprocess import process_timetable
from responses.preprocess import process_braces
from responses.preprocess import process_sad_braces

responses_plain = {}

responses_regexp = {
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

    '(?i)^\s*расписание': {
        'message': '%timetable%',
        'preprocess': process_timetable
    }
}


def init():
    r_plain = database.load_plain_responses()
    r_regexp = database.load_regexp_responses()

    for r in r_plain:
        real_r = {r['trigger']: r['action']}
        responses_plain.update(real_r)

    for r in r_regexp:
        real_r = {r['regexp']: r['action']}
        responses_regexp.update(real_r)
