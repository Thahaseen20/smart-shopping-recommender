import sqlite3

class DataCollector:
    def __init__(self, db="ecom.db"):
        self.conn = sqlite3.connect(db)

    def log(self, user_id, product_id, action):
        self.conn.execute(
            "INSERT INTO behavior (user_id, product_id, action, timestamp) VALUES (?, ?, ?, datetime('now'))",
            (user_id, product_id, action)
        )
        self.conn.commit()
