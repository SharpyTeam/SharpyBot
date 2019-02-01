from pymongo import MongoClient

import config

mdb_c = None
mdb = None


def init():
    global mdb_c, mdb
    print("Connecting to MongoDb server (%s)..." %
          (config.mdb_host + ':' + config.mdb_port))
    mdb_c = MongoClient(config.mdb_host + ':' + config.mdb_port,
                        username=config.mdb_user,
                        password=config.mdb_password,
                        authMechanism='SCRAM-SHA-1',
                        connect=False)
    print("Accessing 'sharpybot' database...")
    mdb = mdb_c.sharpybot
    print("Connected. MongoDb version: " + mdb_c.server_info()['version'])


def load_plain_responses():
    global mdb_c, mdb
    print("Fetching plain responses...")
    r = []
    c = 0

    for a in mdb.responses_plain.find():
        r.append(a)
        c += 1

    print("Fetched " + str(c) + " plain responses")
    return r


def load_regexp_responses():
    global mdb_c, mdb
    print("Fetching regexp responses...")
    r = []
    c = 0

    for a in mdb.responses_regexp.find():
        r.append(a)
        c += 1

    print("Fetched " + str(c) + " regexp responses")
    return r
