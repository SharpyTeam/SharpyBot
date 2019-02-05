import re


def can_evaluate_message(message):
    return re.search(r'(?i)^\s*расписание', message) is not None


def evaluate_message(message):
    print('Evaluating:\n' + message + '\n...')
