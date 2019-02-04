import requests
import urllib3

from sharpy import config
from sharpy.database import mdb


def update():
    print("Updating groups from API...")
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    groups = requests.get(
        config.old_api_url + '/groups?facultyoid=0',
        verify=False).json()
    print("Successfully fetched %d groups" % len(groups))
    print("Removing old groups from database...")
    mdb.study_groups.delete_many({})
    print("Removed all groups")
    print("Adding newly fetched groups to database...")
    mdb.study_groups.insert_many(groups)
    print("Successfully updated groups")


def get(group_id):
    return mdb.study_groups.find_one({'groupOid': group_id})


def get_by_name(group_name):
    return mdb.study_groups.find_one({'number': group_name})


def init():
    pass
