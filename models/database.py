import sqlite3
import os

DB_PATH = "data/finance.db"

# This function connects to the database file data/finance.db
def get_connection():
    return sqlite3.connect(DB_PATH)

# Ensure that the path exists, execute database connection, create the transactions table
# if it does not exist
def init_db():
    os.makedirs("data", exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL,
                   date TEXT NOT NULL,
                   type TEXT CHECK(type IN ('Income', 'Expense'))
                   )

"""
    )
