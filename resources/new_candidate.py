from datetime import datetime
from flask import request
from flask_restful import Resource
import time

import confPass
from pymongo import MongoClient


class NewCandidate(Resource):
    def __init__(self):
        client = MongoClient('mongodb://' + confPass.passw['user'] + ':' + confPass.passw['mongoPass'] + '@ds035985.mongolab.com:35985/recruiter')
        db = client.recruiter
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
