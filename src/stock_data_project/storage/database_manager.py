import sqlite3

import pandas as pd


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to {self.db_name}: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print(f"Connection to {self.db_name} closed")

    def execute_query(self, query, parameters=None):
        try:
            if not self.conn:
                self.connect()
            cursor = self.conn.cursor()
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None


class AppDatabase(DatabaseConnection):
    def __init__():
        super().__init__("app.db")

    def get_stock_info(self):
        self.connect()
        query = "SELECT * FROM stocks;"
        result = self.execute_query(query)
        self.close()
        return pd.DataFrame(result)
