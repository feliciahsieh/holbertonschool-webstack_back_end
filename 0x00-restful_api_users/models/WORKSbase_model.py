#!/usr/bin/python3
"""
base_model.py - definition of base_model class
"""

import datetime
import uuid
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# from sqlalchemy import inspect


# Base = declarative_base()

class BaseModel:
    """
    BaseModel definition
    """
    id = None
    created_at = None
    updated_at = None
    # id = Column(String(60), nullable=False, primary_key=True)
    # created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    # updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self):
        """ __init__() - initialized BaseModel object
        Arguments: N/A
        Returns: N/A
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.datetime.now()
