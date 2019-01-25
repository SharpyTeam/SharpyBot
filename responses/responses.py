import database
from responses.preprocess import process_timetable
from responses.preprocess import process_braces
from responses.preprocess import process_sad_braces

responses_plain = {}

# This dict only contains responses with "preprocessing" functions
# Other responses with regular expressions are stored in the database
responses_regexp = {
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
