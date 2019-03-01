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

    @classmethod
    def count(cls):
        """
        count() - returns number of instances of a class
        """
        from models import db_session
        from sqlalchemy import func

        return db_session.query(cls.created_at).count()

    @classmethod
    def get(cls, id):
        """
        get() - returns instance of cls with specific id
        """
        from models import db_session

        result = db_session.query(cls).filter(cls.id == id).first()
        if result is None:
            return None
        if id is None or type(id) is not str:
            return None

        return result

    @classmethod
    def first(cls):
        """
        first() - returns first instance of cls based on created_at
        """
        from models import db_session
        from sqlalchemy import asc

        result = db_session.query(cls).order_by(
            cls.created_at.asc()).limit(1).all()[0]
        return result

    @classmethod
    def last(cls):
        """
        last() - returns last instance of cls based on created_at
        """
        from models import db_session
        from sqlalchemy import desc

        result = db_session.query(cls).order_by(
            cls.created_at.desc()).limit(1).all()[0]
        return result
