import mysql.connector
from datetime import datetime
import os
from urllib.parse import urlparse

def connect_to_mysql():
    """Connect to the MySQL database."""
    mysql_url = os.environ.get("MYSQL_URL")
    
    if not mysql_url:
        raise ValueError("MYSQL_URL environment variable is not set")

    # Parse the URL
    url = urlparse(mysql_url)

    # Establish connection
    db = mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path.lstrip('/'),  # Remove leading slash from path
        port=url.port or 3306  # Default MySQL port
    )
    
    return db

def initialize_chat_history_table(db):
    """Create the chat_history table if it doesn't exist."""
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        role ENUM('user', 'system'),
        content TEXT
    )
    """)
    db.commit()

def save_chat_message(db, role, content):
    """Save a chat message to the database."""
    cursor = db.cursor()
    timestamp = datetime.now()
    cursor.execute("INSERT INTO chat_history (timestamp, role, content) VALUES (%s, %s, %s)",
                   (timestamp, role, content))
    db.commit()

def fetch_chat_history(db):
    """Fetch the entire chat history from the database."""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM chat_history ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    history = [{'id': row[0], 'timestamp': row[1], 'role': row[2], 'content': row[3]} for row in rows]
    return history