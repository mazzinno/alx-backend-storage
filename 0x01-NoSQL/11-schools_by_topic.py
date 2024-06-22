#!/usr/bin/env python3

""" Returning the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """ will List of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
