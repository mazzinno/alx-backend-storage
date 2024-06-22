#!/usr/bin/env python3

""" Change all topics of a school document based on the name
"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
