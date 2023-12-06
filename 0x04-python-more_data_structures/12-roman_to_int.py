#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    index = 0
    for char in roman_string:
        current_value = roman[char]
        if index > 0 and current_value > roman[roman_string[index - 1]]:
            result += current_value - 2 * roman[roman_string[index - 1]]
        else:
            result += current_value
        index += 1
    return result
