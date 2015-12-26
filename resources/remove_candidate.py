from flask import request
from flask_restful import Resource
from bson.objectid import ObjectId

from pymongo import MongoClient


class RemoveCandidate(Resource):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.dataBase
        self.candidates = self.db.candidates

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
