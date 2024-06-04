import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS redeemed_codes (
                            id INTEGER PRIMARY KEY,
                            code TEXT UNIQUE
                            )''')
        self.conn.commit()

    def check_duplicate_code(self, code):
        self.cur.execute("SELECT * FROM redeemed_codes WHERE code = ?", (code,))
        result = self.cur.fetchone()
        return True if result else False

    def insert_code(self, code):
        try:
            self.cur.execute("INSERT INTO redeemed_codes (code) VALUES (?)", (code,))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def close_connection(self):
        self.conn.close()