#!/usr/bin/python3
"""
user.py - class definition of User
"""

import hashlib
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

    @property
    def password(self):
        """
        Getter for password
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Setter for password
        """
        if value is None or type(value) is not str:
            self._password = None
        else:
            value = value.lower()
            a = hashlib.md5(value.encode()).hexdigest()
            self._password = a

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

        return self.first_name + " " + self.last_name

    def __str__(self):
        return "[User] {} - {} - {}".format(
            self.id, self.email, self.display_name())
