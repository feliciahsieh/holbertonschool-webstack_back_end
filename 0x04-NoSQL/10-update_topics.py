#!/usr/bin/python3
""" 10-update_topics.py - change school topics based on name """

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update_topics() - update all topics of school document based on name
    Arguments:
    mongo_collection - pymongo collection
    name - string type. Filtering value
    topics - update with this list of strings
    """
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update(myquery, newvalues)
