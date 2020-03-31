import sqlite3


class DB(object):

    def __init__(self):
        self.db = None
        self.cursor = None
        self.connected = False
        self.open_db()

    def open_db(self):
        self.db = sqlite3.connect('../mastermind.db')
        self.cursor = self.db.cursor()
        self.connected = True

    def execute(self, query, bindings):
        self.open_db()
        cur = self.db.cursor()
        cur.execute(query, bindings)

    def query(self, query, bindings=None):
        self.open_db()
        curs = self.db.cursor()
        if bindings:
            curs.execute(query, bindings)
        else:
            curs.execute(query)

        while True:
            row = curs.fetchone()
            if not row:
                return None
            yield row

            self.close()

    def close(self):
        self.db.commit()
        self.db.close()
        self.connected = False

