import os
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
cors = CORS()

# instantiate the app
app = Flask(__name__)
cors.init_app(app)
api = Api(app)


class SimulationsPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


api.add_resource(SimulationsPing, "/simulations/ping")
