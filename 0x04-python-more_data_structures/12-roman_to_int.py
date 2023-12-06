#!/usr/bin/python3
ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    result = 0
    for index, char in enumerate(roman_string):
        current_value = ROMAN[char]
        if index > 0 and current_value > ROMAN[roman_string[index - 1]]:
            result += current_value - 2 * ROMAN[roman_string[index - 1]]
        else:
            result += current_value
    return result
