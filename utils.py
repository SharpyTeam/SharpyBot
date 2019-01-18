import re

import plural_ru


def find_plural_forms(str):
    m = re.search(r"(?i)%plurals=\((.*)\|(.*)\|(.*)\)%", str)
    return list(m.groups())


def get_plural(n, forms):
    return plural_ru.ru(n, forms)


def remove_auxiliary(str):
    return re.sub(r"(?i)%plurals=\((.*)\|(.*)\|(.*)\)%", "", str)
