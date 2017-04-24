import config
import mysql.connector

config = config.get_config()


class MySQLHelper:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def insert_data(self, query):
        self.cursor.execute(*query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
