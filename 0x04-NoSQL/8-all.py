#!/usr/bin/python3
""" 8-all.py """

import pymongo


def list_all(mongo_collection):
    """ list_all() - list all elements of a collection
    Arguments:
       mongo_collection: pymongo collections object
    Returns: list of documents or None
    """
    if mongo_collection.find_one() is None:
        return []
    return mongo_collection.find()
