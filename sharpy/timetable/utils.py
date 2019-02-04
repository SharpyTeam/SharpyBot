import re


def type_to_abbreviation(s_type):
    words = re.split(r'\W', s_type, flags=re.IGNORECASE)
    return ''.join([word[0] for word in words]).upper()


def generate_sep(date_length):
    return '-' * int(date_length * 2 + 1)
