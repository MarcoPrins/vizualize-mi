from flask_script import Command
import os
import sqlite3
from sqlite3 import Error
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

class SeedCommand(Command):
    """ Seed the DB."""
    def run(self):
      try:
        print("Seeding data")
        conn = sqlite3.connect(app.config['DB_NAME'])
        file_path = os.path.join(app.config['PROJECT_ROOT'], 'seed_data.sql')
        sql_statements = open(file_path).read()
        with conn:
          cursor = conn.cursor()
          cursor.executescript(sql_statements)
          conn.commit()
        conn.close()
        print("All data seeded")
      except Error as err:
        print(str(err))

