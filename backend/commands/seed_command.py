from flask_script import Command
import os
import sqlite3
from sqlite3 import Error
from flask import Flask, current_app


class SeedCommand(Command):
    """ Seed the DB."""
    def run(self):
      try:
        print("Seeding data")
        conn = sqlite3.connect(current_app.config['DB_NAME'])
        file_path = os.path.join(current_app.config['PROJECT_ROOT'], 'fixtures/seed_data.sql')
        sql_statements = open(file_path).read()
        with conn:
          cursor = conn.cursor()
          cursor.executescript(sql_statements)
          conn.commit()
        conn.close()
        print("All data seeded")
      except Error as err:
        print(str(err))

