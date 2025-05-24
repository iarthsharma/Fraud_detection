### fraud_detection_portal/backend/database/db.py

import psycopg2
import json

def insert_prediction(features, prediction, explanation):
    conn = psycopg2.connect(
        dbname="frauddb", user="postgres", password="password", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            features TEXT,
            prediction INTEGER,
            explanation TEXT
        )
    """)
    cur.execute(
        "INSERT INTO predictions (features, prediction, explanation) VALUES (%s, %s, %s)",
        (json.dumps(features), prediction, json.dumps(explanation))
    )
    conn.commit()
    cur.close()
    conn.close()