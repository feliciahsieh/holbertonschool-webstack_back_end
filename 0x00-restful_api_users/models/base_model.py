#!/usr/bin/python3
"""
base_model.py - definition of base_model class
"""
import datetime
import uuid


class BaseModel:
    """
    BaseModel definition
    """
    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        """ __init__() - initialized BaseModel object
        Arguments: N/A
        Returns: N/A
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.datetime.now()
