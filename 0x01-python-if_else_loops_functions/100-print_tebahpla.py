#!/usr/bin/python3
for c in range(122, 96, -1):
    print("{:c}".format(c - 32 * (c % 2)), end="")
