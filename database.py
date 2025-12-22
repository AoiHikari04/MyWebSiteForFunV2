import sqlite3
import hashlib
import os

DATABASE_PATH = 'users.db'

def init_database():
    """Initialize the SQLite database and create users table"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Hash the admin password
    admin_password = "admin"
    password_hash = hashlib.sha256(admin_password.encode()).hexdigest()
    
    # Insert admin user (or update if exists)
    cursor.execute('''
        INSERT OR REPLACE INTO users (id, username, password_hash, email)
        VALUES (1, 'admin', ?, 'admin@example.com')
    ''', (password_hash,))
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")
    print("Admin user created with username: 'admin' and password: 'admin'")

def get_user_by_username(username):
    """Get user by username from database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    conn.close()
    return user

def verify_password(password, password_hash):
    """Verify password against stored hash"""
    return hashlib.sha256(password.encode()).hexdigest() == password_hash

def update_user_password(user_id, new_password):
    """Update user password with new hashed password"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Hash the new password
    new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
    
    cursor.execute('UPDATE users SET password_hash = ? WHERE id = ?', (new_password_hash, user_id))
    conn.commit()
    conn.close()
    
    return cursor.rowcount > 0  # Returns True if update was successful

if __name__ == '__main__':
    init_database()