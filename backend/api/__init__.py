import sqlite3
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.simulations import Simulations

# Instantiate the app
app = Flask(__name__)

# Configure environment
if app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "test":
    app.config.from_object("config.TestingConfig")
elif app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")

# Instantiate CORS and flask_restful api
cors = CORS()
cors.init_app(app)
api = Api(app)

api.add_resource(Simulations, "/simulations")
