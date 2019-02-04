import re

import plural_ru


def find_plural_forms(the_str):
    m = re.search(r"(?i)%plurals=\((.*)\|(.*)\|(.*)\)%", the_str)
    return list(m.groups())


def get_plural(n, forms):
    return plural_ru.ru(n, forms)


def remove_auxiliary(the_str):
    return re.sub(r"(?i)%plurals=\((.*)\|(.*)\|(.*)\)%", "", the_str)
