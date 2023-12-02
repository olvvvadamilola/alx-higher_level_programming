#!/usr/bin/python3
def no_c(my_string):
    if not isinstance(my_string, str):
        return None

    result = ''
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return (result)
