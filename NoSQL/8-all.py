#!/usr/bin/env python3
"""Function that lists all documents in a collection of mongoDB."""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Function that returns a lists all documents."""
    all_docs = mongo_collection.find()
    if not all_docs:
        return []
    return all_docs
