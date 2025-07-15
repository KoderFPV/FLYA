from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoDBClient:
    def __init__(self, mongo_uri: str, mongo_db_name: str):
        self._client = None
        self._db_name = mongo_db_name
        self._connect(mongo_uri)

    def _connect(self, mongo_uri: str):
        try:
            self._client = MongoClient(mongo_uri)
            self._client.admin.command("ping")
            print(
                f"Successfully connected to MongoDB: {mongo_uri}, "
                f"database: {self._db_name}"
            )
        except ConnectionFailure as e:
            print(f"MongoDB connection error: {e}")
            self._client = None
        except Exception as e:
            print(
                f"An unexpected error occurred while connecting to MongoDB: {e}")
            self._client = None

    def get_db(self):
        if self._client and self._db_name:
            return self._client[self._db_name]
        else:
            raise Exception("No active MongoDB connection or database name.")

    def close_connection(self):
        if self._client:
            self._client.close()
            print("MongoDB connection closed.")
            self._client = None
