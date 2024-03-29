#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic."""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """"Function that returns the list."""
    return mongo_collection.find({"topics": topic})
