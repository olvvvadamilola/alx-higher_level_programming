#!/usr/bin/python3
""" 7-base_geometry.py """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ Raise an Exception with message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value as an integer and its positivity """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
