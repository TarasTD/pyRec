from flask_restful import Resource
import flask

from pymongo import MongoClient
import confPass

client = MongoClient('mongodb://' + confPass.passw['user'] + ':' + confPass.passw['mongoPass'] + '@ds035985.mongolab.com:35985/recruiter')
# client = MongoClient()

db = client.recruiter
# db = client.dataBase


candidates = db.candidates


class Reader(Resource):
    def get(self):
        amount = candidates.count()
        a = candidates.find_one()
        b = db.collection_names()
        c = candidates.find()
        d = {}
        # print c
        for i in c:
            if "_id" in i:
                i['_id'] = str(i['_id'])
            d.update({i['_id']: i})
        # return str(d)
        # print d
        return flask.jsonify(d)
