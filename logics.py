import random
import re

from responses import *


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
