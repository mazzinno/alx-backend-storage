#!/usr/bin/env python3
'''
inserting a new document in a collection
'''


def insert_school(mongo_collection, **kwargs):
    '''
    will insert a new document in a collection
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
