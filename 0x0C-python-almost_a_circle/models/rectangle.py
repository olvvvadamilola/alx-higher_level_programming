#!/usr/bin/python3
"""Defines a Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x coordinate of rectangle. Defaults to 0.
        y (int): y coordinate of rectangle. Defaults to 0.
        id (int): id of rectangle. Defaults to None.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height
    
    def display(self):
        """Print the Rectangle instance with '#' characters."""
        for _ in range(self.__height):
            print("#" * self.__width)
