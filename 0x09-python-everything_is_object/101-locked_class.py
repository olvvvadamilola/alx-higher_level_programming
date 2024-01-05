#!/usr/bin/python3
"""define a locked class"""


class LockedClass:
    """override the __setattr__ method to control attribute assignment"""
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            msg = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(msg.format(name))
