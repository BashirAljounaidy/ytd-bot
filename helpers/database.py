import sqlite3


class Database:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

        # create table if not exists
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS yt_urls (urls TEXT PRIMARY KEY)"""
        )

    def check_url(self, url):
        """
        This method checks if the url exists in the database if yes will return none. If it does not exist, it adds it to the database and return the url.
        """
        self.cursor.execute("SELECT * FROM yt_urls WHERE urls=?", (url,))
        result = self.cursor.fetchone()

        # If the item does not exist in the database, add it to the new list
        if result is None:
            return url
        # Return the new list of items
        return None

    def add_url(self, url):
        self.cursor.execute("INSERT INTO yt_urls (urls) VALUES (?)", (url,))
        self.conn.commit()
        print("Url Added to database")
        return url

    def close(self):
        self.cursor.close()
        self.conn.close()
