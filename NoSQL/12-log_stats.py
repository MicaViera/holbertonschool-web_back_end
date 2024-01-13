#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    num_documents = nginx_collection.countDocuments()
    print(f"{num_documents} logs")
    print("Methods:")
    num_GET = nginx_collection.countDocuments({"method": "GET"})
    print(f"/tmethod GET:{num_GET}")
    num_POST = nginx_collection.countDocuments({"method": "POST"})
    print(f"/tmethod GET:{num_POST}")
    num_PUT = nginx_collection.countDocuments({"method": "PUT"})
    print(f"/tmethod GET:{num_PUT}")
    num_PATCH = nginx_collection.countDocuments({"method": "PATCH"})
    print(f"/tmethod GET:{num_PATCH}")
    num_DELETE = nginx_collection.countDocuments({"method": "DELETE"})
    print(f"/tmethod GET:{num_DELETE}")
    num_status = nginx_collection.countDocuments({"path": "/status"})
    print(f"{num_status} status check")
