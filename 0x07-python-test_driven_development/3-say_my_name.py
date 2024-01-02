#!/usr/bin/python3
"""define a function that prints full name"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name.

    Args:
        first_name (str): A string representing the first name.
        last_name (str, optional): A string representing the last name.
        Defaults to "".

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Returns:
        None. The function prints the full name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
