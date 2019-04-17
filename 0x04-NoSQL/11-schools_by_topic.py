#!/usr/bin/python3
""" 11-schools_by_topic.py - get list of schools filtered by specific topic """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic() - find list of schools with specific topics
    Arguments:
    mongo_collection - pymongo collection object
    topic - filtering value
    Returns: list of schools (string)
    """
    query = {"topics": topic}
    return mongo_collection.find(query)
