#!/usr/bin/python3

def print_square(size):
    """
    Prints a square made of '#' characters.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for a in range(size):
        print('#' * size)
