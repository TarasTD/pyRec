from datetime import datetime
from flask import request
from flask_restful import Resource
import time

from pymongo import MongoClient


class NewCandidate(Resource):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.dataBase
        self.candidates = self.db.candidates

    def post(self):
        name, surname = self.__request_fields()
        new_candidate = self.__create(name, surname)
        self.result = self.candidates.insert_one(new_candidate)
        return str(self.result.inserted_id)

    def __create(self, name, surname):
        return {
            'name': name,
            'surname': surname,
            "created": time.time()
        }

    def __request_fields(self):
        json = request.json
        return json['name'], json['surname']
