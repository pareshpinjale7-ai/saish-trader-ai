# database_engine.py

import sqlite3

# =========================
# DB CONNECT
# =========================

conn = sqlite3.connect(

    "scanner.db",

    check_same_thread=False

)

cursor = conn.cursor()

# =========================
# CREATE TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS signals (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symbol TEXT,

    signal TEXT,

    rfact REAL,

    probability REAL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

""")

conn.commit()

# =========================
# SAVE SIGNAL
# =========================

def save_signal(

    symbol,
    signal,
    rfact,
    probability

):

    cursor.execute("""

    INSERT INTO signals (

        symbol,
        signal,
        rfact,
        probability

    )

    VALUES (?, ?, ?, ?)

    """, (

        symbol,
        signal,
        rfact,
        probability

    ))

    conn.commit()