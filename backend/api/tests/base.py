from flask_restful import Api
from flask import Flask
from flask_cors import CORS
from flask_testing import TestCase

from api.tests import app, routes

class BaseTestCase(TestCase):
    def create_app(self):
        cors = CORS()
        cors.init_app(app)
        api = Api(app)
        return app
