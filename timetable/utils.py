import re


def type_to_abbreviation(s_type):
    words = re.split(r'\W', s_type, flags=re.IGNORECASE)
    return ''.join([word[0] for word in words]).upper()
