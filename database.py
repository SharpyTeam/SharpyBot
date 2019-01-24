from pymongo import MongoClient

import settings


class Db:
    mdb = None

    def __init__(self):
        print("Connecting to MongoDB...")
        self.mdb = MongoClient(settings.mdb_host + ':' + settings.mdb_port,
                               username=settings.mdb_user,
                               password=settings.mdb_password,
                               authMechanism='SCRAM-SHA-1')
        print("Connected. MongoDb version " + self.mdb.server_info().version)

