#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Class defining a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the instance"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
