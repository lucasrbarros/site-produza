# database.py

import sqlite3

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # Permite acessar as colunas por nome
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Cria a tabela de usuários se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            drive_link TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Banco de dados inicializado com sucesso!")
