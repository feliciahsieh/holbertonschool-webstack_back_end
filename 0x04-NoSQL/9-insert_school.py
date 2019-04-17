#!/usr/bin/python3
""" 9-insert_school.py """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert_school() - insert documents into collection
    Arguments:
       mongo_collection: pymongo collections object
       kwargs: data set
    Returns: _id of created object
    """
    return mongo_collection.insert(kwargs)
