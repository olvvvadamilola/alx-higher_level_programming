#!/usr/bin/python3
"""Defines a function that checks if an
object is an instance or inherited"""


def inherits_from(obj, a_class):
    """ checks if an object is an instance or
    inherited instance of a class """
    return isinstance(obj, a_class)
