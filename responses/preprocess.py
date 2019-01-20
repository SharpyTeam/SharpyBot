import re

import utils


def process_braces(m_vars):
    braces_count = len(re.findall(r'\)', m_vars['message']))
    m_vars['braces_message'] = str(braces_count) + ' ' + utils.get_plural(braces_count,
                                                                          ['скобочка', 'скобочки', 'скобочек'])
    m_vars['braces_count'] = braces_count


def process_sad_braces(m_vars):
    sad_braces_count = len(re.findall(r'\(', m_vars['message']))
    sad_plurals = ['грустная скобочка', 'грустные скобочки', 'грустных скобочек']
    m_vars['sad_braces_message'] = str(sad_braces_count) + ' ' + utils.get_plural(sad_braces_count, sad_plurals)
    m_vars['sad_braces_count'] = sad_braces_count
