#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        return int(value)
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
