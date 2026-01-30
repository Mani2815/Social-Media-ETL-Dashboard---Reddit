import sqlite3
import json
import os

def load_to_sqlite(processed_file):
    # Database path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "database", "social_media.db")

    # Ensure database folder exists
    os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)

    # Connect to DB
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caption TEXT,
            sentiment REAL,
            likes INTEGER,
            image_url TEXT,
            timestamp TEXT,
            hashtags TEXT
        )
    """)

    # Load processed JSON
    with open(processed_file, "r") as f:
        data = json.load(f)

    # Insert each post
    for post in data:
        cur.execute("""
            INSERT INTO posts (caption, sentiment, likes, image_url, timestamp, hashtags)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            post["caption"],
            post["sentiment"],
            post["likes"],
            post["image_url"],
            post["timestamp"],
            ",".join(post["hashtags"])
        ))

    conn.commit()
    conn.close()

    print(f"✅ Loaded data into DB → {DB_PATH}")
