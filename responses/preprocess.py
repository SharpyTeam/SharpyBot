import re
import requests
import datetime

from pymongo.collection import Collection

import timetable as t
import timetable.utils
import utils

import urllib3

import database


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
    m = re.search(r'(?i)(?<=расписание)\s*(\w+)\s*', m_vars['message'])
    if m is None:
        m_vars['timetable'] = 'неверный запрос'
        return

    group = m.group(1).strip()

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    groups_search_result = requests.get(
        'https://ruz.hse.ru/api/search?term=' + group + '&type=group',
        verify=False).json()

    if not groups_search_result:
        m_vars['timetable'] = "Группа «" + group + "» не найдена :("
        return

    group_id = groups_search_result[0]['id']

    group_timetable_get_result = requests.get(
        'https://ruz.hse.ru/api/schedule/group/' + str(group_id) +
        '?start=' + datetime.datetime.now().strftime("%Y.%m.%d") +
        '&finish=' + (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y.%m.%d') +
        '&lng=1',
        verify=False)

    timetable_string = 'Расписание группы ' + groups_search_result[0]['label'] + ':\n'

    date = None
    group_timetable_json = group_timetable_get_result.json()
    for entry in group_timetable_json:
        if entry['disciplinetypeload'] == 5 or entry['isBan']:
            continue

        discipline_name = None
        db_disciplines = database.mdb.sharpybot.disciplines
        if not db_disciplines.count_documents({'disciplineOid': entry['disciplineOid']}) > 0:
            db_disciplines.insert_one({
                'discipline': entry['discipline'],
                'disciplineOid': entry['disciplineOid'],
                'short_name': entry['discipline'],
                'disciplinetypeload': entry['disciplinetypeload']
            })
            discipline_name = entry['discipline']
            print("Adding discipline '" + entry['discipline'] + "'")
        else:
            d_entry = db_disciplines.find_one({'disciplineOid': entry['disciplineOid']})
            discipline_name = d_entry['short_name']
            print("Short name for '" + d_entry['discipline'] + "' is '" + discipline_name + "'")

        if date != entry['date']:
            timetable_string += '\n'
            fixed_date = '.'.join(str(entry['date']).split('.')[::-1])
            date_str = fixed_date + ' ' + entry['dayOfWeekString']
            sep = t.utils.generate_sep(len(date_str))
            timetable_string += date_str + '\n' + sep + '\n'
            date = entry['date']

        discipline = re.sub(r'(?i)\(.*?\)$', "", discipline_name)
        tag = t.utils.type_to_abbreviation(entry['kindOfWork']) if entry['kindOfWork'] else '?'
        timetable_string += entry['beginLesson'] + ' - ' + entry['endLesson'] + ' [' + entry['auditorium'] + '] '
        timetable_string += discipline + ' '
        timetable_string += '[' + tag + ']\n '

    if date is None:
        timetable_string = 'нет пар'

    m_vars['timetable'] = timetable_string


if __name__ == '__main__':
    process_timetable({'message': input()})
