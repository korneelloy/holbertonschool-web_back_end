#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_count = collection.count_documents({})
    print(f"{total_count} logs\nMethods:")

    get_count = collection.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get_count}")

    post_count = collection.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post_count}")

    put_count = collection.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put_count}")

    patch_count = collection.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch_count}")

    delete_count = collection.count_documents({"method": "DELETE"})
    print(f"\tmethod DELETE: {delete_count}")

    status_count = collection.count_documents({"path": "/status"})
    print(f"{status_count} status check")
