import os
from flask_script import Command
from flask import current_app
from sqlite3 import Error

from helpers.database import execute_multi_sql


class SeedCommand(Command):
    """ Seed the DB."""
    def run(self):
        create_tables = os.path.join(current_app.config['PROJECT_ROOT'], 'fixtures/create_tables.sql')
        seed_data = os.path.join(current_app.config['PROJECT_ROOT'], 'fixtures/seed_data.sql')
        try:
          execute_multi_sql(open(create_tables).read() + open(seed_data).read())
          print('All data seeded')
        except Error as err:
          print(str(err))

