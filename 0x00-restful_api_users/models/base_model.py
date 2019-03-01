#!/usr/bin/python3
"""
base_model.py - definition of base_model class
"""

from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String

""" SQLAlchemy returns a new Base class from which all mapped
classes should inherit. When the class definition is completed,
a new Table and mapper() will have been generated
"""
Base = declarative_base()


class BaseModel:
    """
    BaseModel definition
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self):
        """ __init__() - initialized BaseModel object
        Arguments: N/A
        Returns: N/A
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = str(datetime.utcnow())

    @classmethod
    def all(cls):
        """
        all() - returns a dictionary of all the objects depending on the class.
        Using @classmethod so the class, a session, & attribute can be passed
        """
        from models import db_session

        query = db_session.query(cls).order_by(cls.created_at).all()
        return(query)
