#!/usr/bin/python3
"""working on basemodel"""
import uuid
from datetime import datetime


class BaseModel:
    """Creates basemodel class."""
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints class name."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """Updates updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dic(self):
        """returns a dictionary."""

        return self.__dict__
