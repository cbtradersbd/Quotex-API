import sqlite3

class CandleDatabase:
    def __init__(self, db_path="candles_history.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS candles 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, pair TEXT, timestamp INT, open REAL, high REAL, low REAL, close REAL, payout INT)''')
