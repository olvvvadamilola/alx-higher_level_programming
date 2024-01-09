#!/usr/bin/python3
""" Module for Square Class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initialize square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Return area of square """
        return self.__size * self.__size

    def __str__(self):
        """ Return string representation of square """
        return "[Square] {}/{}".format(self.__size, self.__size)
