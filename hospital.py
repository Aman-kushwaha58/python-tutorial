from pymongo import MongoClient

# Replace with your MongoDB connection string
MONGO_URI = "mongodb://localhost:27017/"  

# Establish a connection to MongoDB
client = MongoClient(MONGO_URI)

# Select a database
db = client["aman_library"]  # Replace with your database name

# Select a collection
collection = db["books"]  # Replace with your collection name

# Insert a test document
test_document = {"name": "Alice", "age": 25, "city": "New York"}
inserted_id = collection.insert_one(test_document).inserted_id
print(f"Inserted document with ID: {inserted_id}")

# Fetch and print a document
retrieved_doc = collection.find_one()
print("Retrieved document:", retrieved_doc)

# ---------------- UPDATE Operation ----------------
update_filter = {"name": "Alice"}  # Find document where name is Alice
new_values = {"$set": {"age": 26, "city": "San Francisco"}}  # New data

updated_result = collection.update_one(update_filter, new_values)
print(f"Modified documents count: {updated_result.modified_count}")

# Verify update
updated_doc = collection.find_one({"name": "Alice"})
print("Updated document:", updated_doc)

# ---------------- DELETE Operation ----------------
delete_filter = {"name": "Alice"}  # Find document where name is Alice

deleted_result = collection.delete_one(delete_filter)
print(f"Deleted documents count: {deleted_result.deleted_count}")

# Verify delete
deleted_doc = collection.find_one({"name": "Alice"})
print("After delete, document found:", deleted_doc)  # Should print None

# Close the connection (optional)
client.close()
