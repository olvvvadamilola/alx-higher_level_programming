#!/usr/bin/python3
""" function that prints a text with
2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """define function

    Args:
        text (str): string

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_c = ('.', '?', ':')
    current_line = ""

    for char in text:
        if current_line in new_line_c and char == " ":
            continue
        print(char, end='')
        print('\n' * 1) if char in new_line_c else None
        current_line = char
