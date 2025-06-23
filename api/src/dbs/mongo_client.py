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
            self._client.admin.command('ping')
            print(f"Successfully connected to MongoDB: {
                  mongo_uri}, database: {self._db_name}")
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


# --- Example Usage ---
if __name__ == "__main__":
    MONGO_URI = "mongodb://localhost:27017/"
    MONGO_DB_NAME = "my_app_database_no_singleton"

    # First instance creation - establishes a connection
    db_client1 = MongoDBClient(MONGO_URI, MONGO_DB_NAME)
    db1 = db_client1.get_db()
    print(f"Database for db_client1: {db1.name}")

    # Second instance creation - establishes a NEW connection
    db_client2 = MongoDBClient(MONGO_URI, MONGO_DB_NAME)
    db2 = db_client2.get_db()
    print(f"Database for db_client2: {db2.name}")

    # They are now distinct instances and connections
    print(f"Are db_client1 and db_client2 the same instance? {
          db_client1 is db_client2}")
    print(f"Is the connection for db_client1 and db_client2 the same? {
          db_client1._client is db_client2._client}")

    # Example database operations
    try:
        users_collection = db1["users"]
        users_collection.insert_one({"name": "Piotr Nowak", "age": 45})
        print("Document added to 'users' collection via db_client1.")

        found_user = users_collection.find_one({"name": "Piotr Nowak"})
        print(f"Found user via db_client1: {found_user}")
    except Exception as e:
        print(f"An error occurred during database operation: {e}")
    finally:
        db_client1.close_connection()
        db_client2.close_connection()  # Remember to close all connections!

    # Attempt to use after closing db_client1 - db_client2 might still work (if not closed)
    try:
        # If db_client1 was closed, this will fail
        db1.command('ping')
    except Exception as e:
        print(f"Expected error using db1 after its client was closed: {e}")
