#!/usr/bin/python3
"""Define square class"""


class Square:
    """
    Attributes:
    __size (int): The size of the square.
    __position (tuple): The position of the square.

    Methods:
    __init__: Initializes a square with an optional size and position.
    area: Calculates the area of the square.
    my_print: Prints the square using '#' characters.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with the given size and position.

        Args:
        size (int, optional): The length of each side of the square.
        position (tuple, optional): The position of the square.

        Raises:
        TypeError: If size is not an integer or if position is not a tuple of
        2 positive integers.
        ValueError: If size or position values are invalid.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 \
                or not all(isinstance(val, int) for val in position) \
                or not all(val >= 0 for val in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(val, int) for val in value) \
                or not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters with the given position.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
