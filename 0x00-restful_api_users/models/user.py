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

    def display_name(self):
        """
        display_name() - displays full name of User instance
        """
        if self.id is None and self.first_name is None \
           and self.last_name is None:
            return ""

        if self.first_name is None and self.last_name is None:
            return self.email

        if self.last_name is None:
            return self.first_name

        if self.first_name is None:
            return self.last_name

        return self.first_name + self.last_name
