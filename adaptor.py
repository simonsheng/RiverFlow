import os
import ftplib
import mysql.connector
from azure.cosmos import CosmosClient


class FileAdaptor:
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode

    def read_data(self):
        if self.mode == 'r' and os.path.exists(self.path):
            with open(self.path, 'r') as file:
                return file.readlines()
        return []

    def write_data(self, data):
        if self.mode == 'w':
            with open(self.path, 'w') as file:
                file.writelines(data)


class FTPAdaptor:
    def __init__(self, host, username, password, path, mode='r'):
        self.host = host
        self.username = username
        self.password = password
        self.path = path
        self.mode = mode
        self.connection = ftplib.FTP(self.host)

    def connect(self):
        self.connection.login(self.username, self.password)

    def read_data(self):
        if self.mode == 'r':
            with open("temp.txt", "wb") as f:
                self.connection.retrbinary(f"RETR {self.path}", f.write)
            with open("temp.txt", "r") as file:
                return file.readlines()
        return []

    def write_data(self, data):
        if self.mode == 'w':
            with open("temp.txt", "w") as file:
                file.writelines(data)
            with open("temp.txt", "rb") as f:
                self.connection.storbinary(f"STOR {self.path}", f)


class MySQLAdaptor:
    def __init__(self, host, user, password, database, query, mode='r'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.query = query
        self.mode = mode
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def read_data(self):
        if self.mode == 'r':
            self.cursor.execute(self.query)
            return self.cursor.fetchall()
        return []

    def write_data(self, data):
        if self.mode == 'w':
            for row in data:
                self.cursor.execute(self.query, row)
            self.connection.commit()


class CosmosDBAdaptor:
    def __init__(self, endpoint, key, database, container, query, mode='r'):
        self.endpoint = endpoint
        self.key = key
        self.database = database
        self.container = container
        self.query = query
        self.mode = mode
        self.client = CosmosClient(self.endpoint, credential=self.key)
        self.database_client = self.client.get_database_client(self.database)
        self.container_client = self.database_client.get_container_client(self.container)

    def read_data(self):
        if self.mode == 'r':
            result = list(self.container_client.query_items(query=self.query, enable_cross_partition_query=True))
            return result
        return []

    def write_data(self, data):
        if self.mode == 'w':
            for item in data:
                self.container_client.create_item(body=item)
