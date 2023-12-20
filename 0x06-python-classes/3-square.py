#!/usr/bin/python3
"""Define square class"""


class Square:
    """
    Attributes:
    size (int): The size of the square."""

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

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
