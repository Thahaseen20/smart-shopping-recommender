import sqlite3
import pandas as pd
from sklearn.cluster import KMeans

class SegmentationAgent:
    def __init__(self, db="ecom.db"):
        self.conn = sqlite3.connect(db)

    def segment_users(self):
        df = pd.read_sql("SELECT * FROM users", self.conn)
        if len(df) < 3:
            return {}
        kmeans = KMeans(n_clusters=2, random_state=42)
        df['segment'] = kmeans.fit_predict(df[['age']])
        return df[['user_id', 'segment']].to_dict('records')
