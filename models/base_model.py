#!/usr/bin/python3
"""
AirBnB clone - The console
"""
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            time_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(val, time_format))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """A string representation of an object using the method __str__"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """An update to the attribute updated_at using the method save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A dictionary representation of an object using the method to_dict"""
        dictionnary = self.__dict__.copy()
        dictionnary["__class__"] = self.__class__.__name__dictionnary["created_at"] = self.updated_at.isoformat()
        dictionnary["updated_at"] = self.updated_at.isoformat()
        return dictionnary
