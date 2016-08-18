from flask import request
from flask_restful import Resource
from bson.objectid import ObjectId

import models


class RemoveCandidate(Resource):
    def __init__(self):
        db = models.init_connection()
        self.candidates = db.candidates

    def post(self):
        self.id = self.__request_fields()
        candidate = self.__create(self.id)
        self.result = self.candidates.remove(candidate)
        return str(self.result)

    def __create(self, id):
        return {
            '_id': ObjectId(id),
        }

    def __request_fields(self):
        json = request.json
        return json['id']
