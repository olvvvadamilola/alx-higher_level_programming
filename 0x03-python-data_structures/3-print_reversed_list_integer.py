#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        raise TypeError("`my_list` must be a list")
    for item in reversed(my_list):
        print("{:d}".format(item))
