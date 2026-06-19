# delete_collection.py
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")
client.delete_collection("docs")
print("Collection 'docs' deleted successfully.")