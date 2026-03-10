import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.db"

def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        print("Conexão com o banco realizada com sucesso")
        return conn
    except sqlite3.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None