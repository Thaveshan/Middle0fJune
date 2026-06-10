import sqlite3

DATABASE_NAME = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_users_table():
    conn =get_db_connection()
    conn.execute('''
                 CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        phone TEXT NOT NULL,
                        bio TEXT NOT NULL
                    )
                ''')
    
    conn.commit()
    conn.close()
                