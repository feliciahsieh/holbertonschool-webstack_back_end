#!/usr/bin/python3
"""
user.py - class definition of User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class User definition
    """

    def __init__(self):
        """
        __init() - initialize User object
        """
        self._password = None

        self.email = None
        self.first_name = None
        self.last_name = None
        super().__init__()
