import sqlite3

class RecommendationAgent:
    def __init__(self, db="ecom.db"):
        self.conn = sqlite3.connect(db)

    def recommend_popular(self, user_id, limit=3):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT product_id, COUNT(*) as score
            FROM behavior
            WHERE action = 'purchase'
            GROUP BY product_id
            ORDER BY score DESC
            LIMIT ?
        """, (limit,))
        return cursor.fetchall()
