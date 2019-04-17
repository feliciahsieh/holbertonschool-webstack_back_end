#!/usr/bin/python3
""" 101-students.py - find students sorted by average score """
import pymongo


def top_students(mongo_collection):
    """
    top_students() - find students sorted by average score
    Arguments:
       mongo_collection - pymongo collection object
    Return:
       list of sorted students by avg score. Append avg students' scores
    """
    return mongo_collection.aggregate([
        {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
