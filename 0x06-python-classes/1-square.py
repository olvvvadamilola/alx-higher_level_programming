#!/usr/bin/python3
"""Define square class
    attributes:
        size(int): size of the square(private)
        Return: area of the square"""


class Square:
    """
    This class represents a square.

    Args:
        size (int, optional): The size of the square. Defaults to 0.

    Attributes:
        __size (int): The size of the square.

    Example:
        square1 = Square(5)
        square2 = Square()
    """
    def __init__(self, size=0):
        """Initializing the data"""
        self.__size = size
