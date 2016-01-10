from pymongo import MongoClient
import confPass


def init_connection():
    # client = MongoClient('mongodb://' + confPass.passw['user'] + ':' + confPass.passw['mongoPass'] + '@ds035985.mongolab.com:35985/recruiter')
    client = MongoClient()
    # db = client.recruiter
    db = client.dataBase

    return db
