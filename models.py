# models.py

from flask_login import UserMixin
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

class User(UserMixin):
    def __init__(self, username, password, drive_link, role='user'):
        self.id = username  # Usando 'username' como ID
        self.username = username
        self.password = password
        self.drive_link = drive_link
        self.role = role

    @staticmethod
    def get(username):
        conn = get_db_connection()
        user_row = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user_row:
            return User(user_row['username'], user_row['password'], user_row['drive_link'], user_row['role'])
        return None

    @staticmethod
    def create(username, password, drive_link, role='user'):
        # Utilize 'pbkdf2:sha256' como método de hash
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, drive_link, role) VALUES (?, ?, ?, ?)',
                         (username, hashed_password, drive_link, role))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def verify_password(self, password):
        return check_password_hash(self.password, password)
