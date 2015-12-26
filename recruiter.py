from flask import Flask
from flask_restful import Api
from resources.new_candidate import NewCandidate
from resources.get_all import Reader
from resources.remove_candidate import RemoveCandidate
from resources.get_candidates import GetCandidate


app = Flask(__name__, static_url_path='')

api = Api(app)


@app.route('/')
def redirect_to_index(name=None):
    return app.send_static_file('index.html')

api.add_resource(Reader, '/s')
api.add_resource(NewCandidate, '/new_candidate')
api.add_resource(GetCandidate, '/get_candidate/<string:id>')
api.add_resource(RemoveCandidate, '/remove_candidate')


if __name__ == '__main__':
    app.run(debug=True)
