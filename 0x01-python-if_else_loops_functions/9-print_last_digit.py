#!/usr/bin/python3
def print_last_digit(number):
    lastnum = abs(number) % 10
    print("{}".format(lastnum), end="")
    return (lastnum)
