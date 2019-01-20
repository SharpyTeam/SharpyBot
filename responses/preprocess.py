import re

import utils


def process_braces(m_vars):
    braces_count = len(re.findall('\)', m_vars['message']))
    m_vars['braces_message'] = str(braces_count) + ' ' + utils.get_plural(braces_count,
                                                                          ['скобочка', 'скобочки', 'скобочек'])
    m_vars['braces_count'] = braces_count
