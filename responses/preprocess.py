import re
import requests
import datetime

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


def process_timetable(m_vars):
    m = re.search(r'(?i)(?<=расписание)\s*\w+\s*', m_vars['message'])
    if m is None:
        m_vars['timetable'] = 'неверный запрос'
        return

    group = m[0].strip()

    groups_search_result = requests.get(
        'https://ruz.hse.ru/api/search?term=' + group + '&type=group',
        verify=True)

    group_id = groups_search_result.json()[0]['id']

    group_timetable_get_result = requests.get(
        'https://ruz.hse.ru/api/schedule/group/' + str(group_id) +
        '?start=' + datetime.datetime.now().strftime("%Y.%m.%d") +
        '&finish=' + (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y.%m.%d') +
        '&lng=1',
        verify=True)

    timetable_string = 'Расписание ' + group + ':\n'

    date = None
    for entry in group_timetable_get_result.json():
        if date != entry['date']:
            timetable_string += entry['date'] + ' ' + entry['dayOfWeekString'] + '\n'
            date = entry['date']

        timetable_string += entry['beginLesson'] + ' - ' + entry['endLesson'] + ' ' + entry['discipline'] + '\n'

    if date is None:
        timetable_string = 'нет пар'

    m_vars['timetable'] = timetable_string
