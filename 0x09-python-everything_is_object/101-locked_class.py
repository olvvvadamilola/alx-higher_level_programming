#!/usr/bin/python3
"""define a locked class"""


class LockedClass:
    """override the __setattr__ method to control attribute assignment"""
    def __setattr__(self, name, value):
        """if the attribute name is first_name, allow assignment"""
        if name == "first_name":
            """use the super() function to access the parent class method"""
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 format(name))
