import sqlite3
from datetime import datetime


def get_all_messages(user_id: int, cursor):
    query = f"""
    SELECT * FROM messages WHERE user_id_to = ?
    """
    cursor.execute(query, (user_id,))
    messages = cursor.fetchall()
    cursor.close()
    return messages


def send_message(user_id_from, user_id_to, text, cursor):
    query = """
    INSERT INTO messages
    VALUES
        (NULL, ?, ?, ?, ?)
    """
    cursor.execute(query, (user_id_from, user_id_to, text, datetime.now()))
    cursor.close()


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
        text VARCHAR(50),
        send_time DATETIME
    );
    """
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.close()
