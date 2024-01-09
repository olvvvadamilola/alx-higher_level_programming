#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Class defining a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the instance"""
        return self.__dict__
