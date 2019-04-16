#!/usr/bin/python3
""" 9-insert_school.py """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert_school() - insert documents into collection
    Arguments:
       mongo_collection: pymongo collections object
       kwargs: data set
    Returns: _id
    """
    if mongo_collection.find_one() is None:
        return []

    data = {}
    for x in kwargs:
        data.update({x: kwargs[x]})

    id = mongo_collection.insert(data)
    return id
