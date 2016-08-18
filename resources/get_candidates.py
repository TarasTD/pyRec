from flask_restful import Resource
from bson.objectid import ObjectId
import flask

import models

db = models.init_connection()
candidates = db.candidates


class GetCandidate(Resource):
    def __init__(self):
        db = models.init_connection()
        self.candidates = db.candidates

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
