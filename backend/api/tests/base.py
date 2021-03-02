import os
from flask_restful import Api
from flask import Flask
from flask_cors import CORS
from flask_testing import TestCase

from helpers.database import execute_multi_sql
from api.tests import app

create_tables = os.path.join(app.config['PROJECT_ROOT'], 'fixtures/create_tables.sql')
drop_tables = os.path.join(app.config['PROJECT_ROOT'], 'fixtures/drop_tables.sql')

class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        """ App is imported from the api package to ensure similar setup """
        with app.app_context():
          execute_multi_sql(open(drop_tables).read())
        with app.app_context():
          execute_multi_sql(open(create_tables).read())
        return app
