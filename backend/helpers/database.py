import sqlite3
from sqlite3 import Error
from flask import current_app, g


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DB_NAME'])
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def execute_sql(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute_multi_sql(sql):
    db = get_db()
    with db:
      cursor = db.cursor()
      cursor.executescript(sql)
      db.commit()
    db.close()

