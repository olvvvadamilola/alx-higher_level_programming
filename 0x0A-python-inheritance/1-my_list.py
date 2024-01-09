#!/usr/bin/python3
"""Defines a class MyList"""

class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
