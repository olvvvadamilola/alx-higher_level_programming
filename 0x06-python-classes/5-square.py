#!/usr/bin/python3
"""Define square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with the given size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square."""

        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
