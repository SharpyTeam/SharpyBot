from pymongo import MongoClient

import settings

mdb = None


def init():
    print("Connecting to MongoDB...")
    mdb = MongoClient(settings.mdb_host + ':' + settings.mdb_port,
                      username=settings.mdb_user,
                      password=settings.mdb_password,
                      authMechanism='SCRAM-SHA-1')
    print("Connected. MongoDb info: " + repr(mdb.server_info()))
