import os
from flask_restful import Api
from flask import Flask
from flask_cors import CORS
from flask_testing import TestCase

from helpers.database import execute_multi_sql
from api.tests import app


class BaseTestCase(TestCase):
    def create_app(self):
        create_tables = os.path.join(app.config['PROJECT_ROOT'], 'fixtures/create_tables.sql')
        with app.app_context():
          execute_multi_sql(open(create_tables).read())
        return app
