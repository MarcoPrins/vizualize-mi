import os
import sqlite3
from sqlite3 import Error


def load_data():
  try:
    conn = sqlite3.connect('simulation.db')
    file_path = os.path.join(os.path.dirname(__file__), 'seed_data.sql')
    sql_statements = open(file_path).read()
    with conn:
      cursor = conn.cursor()
      cursor.executescript(sql_statements)
      conn.commit()
    conn.close()
    print("All data seeded")
  except Error as err:
    print(str(err))

