import secrets
import re
import copy

from responses import *


def process_found_entry(regex, command, entry):
    if 'random' in entry:
        entry = secrets.choice(entry['random'])
    if 'message' in entry and '%occurrences%' in entry['message']:
        entry['message'] = copy.deepcopy(entry['message'])
        entry['message'] = entry['message'].replace('%occurrences%', str(len(re.findall(regex, command))))
    return entry


def process_command(command):
    command = command.replace("ё", "е")
    command = command.replace("Ё", "е")
    for k, v in commands.items():
        l_command = r'\s+'.join(re.split(r'\s+', k))
        regex = '(?i)(?<![а-яa-z0-9])' + l_command + '(?![а-яa-z0-9])'
        if re.search(regex, command) is not None:
            return process_found_entry(regex, command, v)

    for k, v in commands_regexp.items():
        if re.search(k, command) is not None:
            return process_found_entry(k, command, v)


if __name__ == '__main__':
    print(process_command(input()))
