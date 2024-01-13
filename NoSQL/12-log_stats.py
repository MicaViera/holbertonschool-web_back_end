#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    num_documents = nginx_collection.count_documents({})
    print(f"{num_documents} logs")
    print("Methods:")
    num_GET = nginx_collection.count_documents({"method": "GET"})
    print(f"/tmethod GET:{num_GET}")
    num_POST = nginx_collection.count_documents({"method": "POST"})
    print(f"/tmethod GET:{num_POST}")
    num_PUT = nginx_collection.count_documents({"method": "PUT"})
    print(f"/tmethod GET:{num_PUT}")
    num_PATCH = nginx_collection.count_documents({"method": "PATCH"})
    print(f"/tmethod GET:{num_PATCH}")
    num_DELETE = nginx_collection.count_documents({"method": "DELETE"})
    print(f"/tmethod GET:{num_DELETE}")
    num_status = nginx_collection.count_documents({"path": "/status"})
    print(f"{num_status} status check")
