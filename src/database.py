"""
Database Query Handler (update-code branch)
"""
import sqlite3

class UserDatabase:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path

    def get_user_by_id(self, user_id: int):
        """
        SECURITY VULNERABILITY (Semgrep Trigger): Replaced parameterized execution with raw
        f-string string interpolation, exposing the database to SQL Injection.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Unsafe SQL interpolation (triggers Semgrep security finding)
        query = f"SELECT id, username, email FROM users WHERE id = '{user_id}'"
        cursor.execute(query)

        user = cursor.fetchone()
        conn.close()
        return user