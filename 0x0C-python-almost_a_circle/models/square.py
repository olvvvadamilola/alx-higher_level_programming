#!/usr/bin/python3
"""Defines a Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for Square.

        Args:
        size (int): size of square
        x (int): x coordinate of square. Defaults to 0.
        y (int): y coordinate of square. Defaults to 0.
        id (int): id of square. Defaults to None.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of Square.

        Returns:
        str: string representation of Square"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square."""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        """Return a list of CSV values for the Square."""
        return [self.id, self.size, self.x, self.y]
