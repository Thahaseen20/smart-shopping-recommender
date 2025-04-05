import sqlite3

class FeedbackAgent:
    def __init__(self, db="ecom.db"):
        self.conn = sqlite3.connect(db)

    def record_feedback(self, user_id, product_id, liked=True):
        action = "like" if liked else "dislike"
        self.conn.execute(
            "INSERT INTO behavior (user_id, product_id, action, timestamp) VALUES (?, ?, ?, datetime('now'))",
            (user_id, product_id, action)
        )
        self.conn.commit()
