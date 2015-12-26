from flask_restful import Resource
from bson.objectid import ObjectId

from pymongo import MongoClient
import flask
import time


class GetCandidate(Resource):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.dataBase
        self.candidates = self.db.candidates

    def get(self, id):
        self.user = self.__create(id)
        res = self.candidates.find_one(self.user)

        try:
            res['_id'] = str(res['_id'])
        except:
            pass

        return flask.jsonify(res)

    def __create(self, id):
        return {
            '_id': ObjectId(id),
        }
