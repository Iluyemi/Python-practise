#!/usr/bin/python3
"""working on basemodel"""
import uuid
from datetime import datetime
format = '%Y-%m-%dT%H:%M:%S.%f'


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
        dic = dict()
        dic.update(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
