#!/usr/bin/python3
"""Define square class
    attributes:
        size(int): size of the square(private)
        Return: area of the square"""

class Square:
    """
    This class represents a square.

    Attributes:
    size (int): The size of the square.

    Methods:
    __init__: Initializes a square with an optional size.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
        size (int, optional): The length of each side of the square.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
