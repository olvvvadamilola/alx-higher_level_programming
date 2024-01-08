#!/usr/bin/python3
""" Defines a function that checks if instance or inherited """


def is_kind_of_class(obj, a_class):
    """ checks if an object is an instance or
    inherited instance of a class """
    return isinstance(obj, a_class)
