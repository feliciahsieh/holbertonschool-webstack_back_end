#!/usr/bin/python3
"""
user.py - class definition of User
"""

import hashlib
from models.base_model import BaseModel


# class User(Base, BaseModel):
class User(BaseModel):
    """
    class User definition
    """

    __tablename__ = 'users'
    email = None
    _password = None
    first_name = None
    last_name = None

    def __init__(self):
        """
        __init() - initialize User object
        """

        # self.email = Column(String(128), nullable=False)
        # self._password = Column(String(128), nullable=False)
        # self.first_name = Column(String(128), nullable=True)
        # self.last_name = Column(String(128), nullable=True)
        self.email = None
        self._password = None
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
            self._password = hashlib.md5(value.encode()).hexdigest()

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

        return "{} {}".format(self.first_name, self.last_name)

    # def __str__(self):
    #    """ __str__() - write custom print statement for User instance
    #    """
    #     return "[User] {} - {} - {}".format(
    #        self.id, self.email, self.display_name())

    def is_valid_password(self, pwd):
        """
        is_valid_password - check if valid password
        Arguments:
        pwd: password to check
        Return True if valid password. False if not
        """
        if pwd is None:
            return False
        if type(pwd) is not str:
            return False
        if self._password is None:
            return False
        if self._password == hashlib.md5(pwd.encode()).hexdigest():
            return True
        return False

    def to_dict(self):
        """
        to_dict() - return a serializable representation of an User instance
        """
        s = self.__dict__
        s['created_at'] = str(s['created_at'])[:-7]
        s['updated_at'] = str(s['updated_at'])[:-7]
        del s['_password']

        return s
