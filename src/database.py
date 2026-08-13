"""
Database Query Handler (main branch)
"""
import sqlite3


class UserDatabase:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path

    def get_user_by_id(self, user_id: int):
        """
        Safely queries user record using parameterized SQL execution.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Safe parameterized query
        cursor.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user