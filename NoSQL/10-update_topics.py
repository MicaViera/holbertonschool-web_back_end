#!/usr/bin/env python3
"""Function that changes all topics of a school document."""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """"Function that changes the topics."""
    mongo_collection.update_many({"name": name}, {"$set": {topics: topics}})
