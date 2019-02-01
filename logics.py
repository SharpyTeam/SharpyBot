import secrets
import copy
import re

from responses.collection import responses_plain, responses_regexp


def process_found_entry(regex, message, entry):
    preprocess = None

    if 'random' in entry:
        # Save preprocessor
        if 'preprocess' in entry:
            preprocess = entry['preprocess']
        entry = secrets.choice(entry['random'])

    if 'message' in entry:
        # Or save it here
        if 'preprocess' in entry:
            preprocess = entry['preprocess']

        m_vars = {
            'message': message,
            'regex': regex
        }

        # Copy for preventing original object changes
        entry = copy.deepcopy(entry)

        # And call preprocessor if exists
        if preprocess is not None:
            preprocess(m_vars)

        # Then substitute var occurrences with their values
        for k, v in m_vars.items():
            entry['message'] = entry['message'].replace('%' + k + '%', str(v))

    return entry


def process_message(message):
    message = message.replace("ё", "е")
    message = message.replace("Ё", "е")
    for k, v in responses_plain.items():
        l_command = r'\s+'.join(re.split(r'\s+', k))
        regex = '(?i)(?<![а-яa-z0-9])' + l_command + '(?![а-яa-z0-9])'
        if re.search(regex, message) is not None:
            return process_found_entry(regex, message, v)

    for k, v in responses_regexp.items():
        if re.search(k, message) is not None:
            return process_found_entry(k, message, v)


if __name__ == '__main__':
    print(process_message(input()))
