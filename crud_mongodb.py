from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus

class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB"""

    def __init__(self):
        # MongoDB Connection Variables
        USER = "aacuser"
        PASS = "pwd123"
        HOST = "nv-desktop-services.apporto.com"
        PORT = 34956
        DB = "AAC"
        COL = "animals"

        # Initialize Connection
        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=AAC")
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the MongoDB collection."""
        if isinstance(data, dict) and data:
            result = self.collection.insert_one(data)
            return result.acknowledged  # Returns True if the insertion is successful
        else:
            raise ValueError("Data must be a non-empty dictionary.")

    def read(self, query):
        """Retrieve documents from the MongoDB collection based on a query."""
        if isinstance(query, dict):
            results = self.collection.find(query)
            return list(results)  # Convert cursor to list
        else:
            raise ValueError("Query must be a dictionary.")

    def update(self, query, update_data):
        """Update one or multiple documents in the MongoDB collection."""
        if isinstance(query, dict) and isinstance(update_data, dict) and query and update_data:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count  # Returns number of modified documents
        else:
            raise ValueError("Query and update_data must be non-empty dictionaries.")

    def delete(self, query):
        """Delete documents from the MongoDB collection."""
        if isinstance(query, dict) and query:
            result = self.collection.delete_many(query)
            return result.deleted_count  # Returns number of deleted documents
        else:
            raise ValueError("Query must be a non-empty dictionary.")