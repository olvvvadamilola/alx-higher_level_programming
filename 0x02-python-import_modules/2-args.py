#!/usr/bin/python3
import sys

if __name__ == "__main__":
    a = sys.argv[1:]
    num_args = len(a)

    if num_args == 0:
        print("{} argument".format(num_args))
    else:
        plural = 'argument' if num_args == 1 else 'arguments'
        print("{} {}:".format(num_args, plural))
        for idx, arg in enumerate(a, 1):
            print("{}: {}".format(idx, arg))
