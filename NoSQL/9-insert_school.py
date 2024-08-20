#!/usr/bin/env python3
"""Insert a document in Python """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Returns the new _id """
    if not mongo_collection:
        return []
    else:
        return mongo_collection.insert_one(kwargs).inserted_id
