#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two numbers together and returns the sum.

    Args:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
    int: The sum of the two numbers.

    Raises:
    TypeError: If 'a' is not an integer or float.
    TypeError: If 'b' is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b
