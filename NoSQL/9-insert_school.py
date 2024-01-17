#!/usr/bin/env python3
"""Function that inserts a new document in collection based on kwargs."""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """"Function that inserts a new document."""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
