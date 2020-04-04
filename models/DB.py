import sqlite3
import os


class DB(object):

    def __init__(self):
        self.db = None
        self.cursor = None
        self.connected = False
        self.open_db()

    def open_db(self):
        self.db = sqlite3.connect(os.path.abspath('./mastermind.db'))
        self.cursor = self.db.cursor()
        self.connected = True

    def execute(self, query, bindings):
        self.cursor.execute(query, bindings)

    def execute_and_return(self, query, bindings=None):
        self.cursor.execute(query, bindings)
        return self.cursor.lastrowid

    def query(self, query, bindings=None):
        self.open_db()
        curs = self.db.cursor()
        if bindings:
            curs.execute(query, bindings)
        else:
            curs.execute(query)
        return curs.fetchall()

    def close(self):
        self.db.commit()
        self.db.close()
        self.connected = False
