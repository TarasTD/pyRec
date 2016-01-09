from flask_restful import Resource
import flask

import models

db = models.init_connection()
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
