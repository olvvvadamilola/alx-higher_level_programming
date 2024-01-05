#!/usr/bin/python3
"""define a locked class"""


class LockedClass:
    """define a locked class"""
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        super().__setattr__(name, value)
