import sqlite3
from datetime import datetime

def get_all_messages(user_id: int, cursor):
    query = """
    SELECT id, user_id_from, user_id_to, text, send_time 
    FROM messages 
    WHERE user_id_to = ?
    ORDER BY send_time DESC
    """
    cursor.execute(query, (user_id,))
    messages = cursor.fetchall()
    return messages

def send_message(user_id_from, user_id_to, text, cursor):
    query = """
    INSERT INTO messages (user_id_from, user_id_to, text, send_time)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (user_id_from, user_id_to, text, datetime.now()))
    cursor.connection.commit()

def create_tables(cursor):
    query1 = """ 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address VARCHAR(50),
        name VARCHAR(50)
    );
    """
    query2 = """ 
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id_from INTEGER,
        user_id_to INTEGER,
        text VARCHAR(500),  -- Увеличил длину текста
        send_time DATETIME
    );
    """
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.connection.commit()

def add_sample_users(cursor):
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    
    if count == 0:
        sample_users = [
            (1, "user1@example.com", "Alice"),
            (2, "user2@example.com", "Bob"),
            (3, "user3@example.com", "Charlie"),
        ]
        
        for user in sample_users:
            cursor.execute("INSERT INTO users (id, address, name) VALUES (?, ?, ?)", user)
        
        cursor.connection.commit()