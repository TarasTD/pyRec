from flask import request
from flask_restful import Resource
import time

import models


class NewCandidate(Resource):
    def __init__(self):
        db = models.init_connection()
        self.candidates = db.candidates

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
