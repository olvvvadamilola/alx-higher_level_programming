#!/usr/bin/python3
"""Define square class"""


class Square:
    """
    Represents a square.

    Attributes:
    __size (int): The size of the square.

    Methods:
    __init__: Initializes a square with a given size.
    area: Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
        size (int/float, optional): The length of each side of the square
        Defaults to 0.
        Raises:
        TypeError: If size is not a number (float or integer).
        ValueError: If size is less than 0.
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator based on square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator based on square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator based on square area."""
        return self.area() <= other.area()
