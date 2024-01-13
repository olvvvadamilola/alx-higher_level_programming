#!/usr/bin/python3
"""Base class for all models, managing object IDs"""


class Base:
    """Base class for all models in project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base object with optional id.

        Args:
        id (int): id of object. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
