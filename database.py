from pymongo import MongoClient
from decouple import config


class Database:
    def __init__(self):
        self.collection = self.configuration()

    def configuration(self):
        host = config("MONGODB_HOST")
        port = int(config("MONGODB_PORT"))
        db_name = config("DB_NAME")
        collection_name = config("COLLECTION_NAME")

        connection = MongoClient(host, port)
        collection = connection[db_name][collection_name]

        return collection
