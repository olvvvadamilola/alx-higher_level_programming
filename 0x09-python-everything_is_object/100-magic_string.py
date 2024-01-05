#!/usr/bin/python3
"""define a magic_string function"""


def magic_string():
    """define a magic_string function"""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.n - 1)
