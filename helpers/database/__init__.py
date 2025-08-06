import psycopg2
from flask import g

from helpers.application import app

DATABASE = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5434',
}

def getConnection():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE)
    return g.db

@app.teardown_appcontext
def closeConnection(exception):
    db = g.pop('db', None)
    if db:
        db.close()