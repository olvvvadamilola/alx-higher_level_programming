#!/usr/bin/python3
"""Defines a Rectangle class."""


class BaseGeometry:
    def area(self):
        """Raises an exception as area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is a positive integer.

        Args:
        - name (str): The name of the value being validated.
        - value (int): The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
