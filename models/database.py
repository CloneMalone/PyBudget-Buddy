# Import SQLite for database operations and OS for file/folder management
import sqlite3
import os
import threading

# Path to where the database file will be stored
DB_PATH = "data/finance.db"

# Get a connection to the database
def get_connection():
    return sqlite3.connect(DB_PATH)

# Create the database and transactions table if they don't exist
def init_db():
    """Create DB and transactions table if they don't exist."""
    # Create the data folder if it doesn't already exist
    os.makedirs("data", exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()

    # Define and create the transactions table with proper structure
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
    conn.commit()
    conn.close()

# Initialize the database on a background thread to avoid freezing the UI
def init_db_background():
    """Initialize the DB on a separate thread so UI is not blocked."""
    # Only initialize if the database doesn't already exist
    if not os.path.exists(DB_PATH):
        # Run init_db on a separate daemon thread
        threading.Thread(target=init_db, daemon=True).start()
