#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, c in enumerate(row):
            if idx < len(row) - 1:
                print("{:d}".format(c), end=" ")
            else:
                print("{:d}".format(c), end="")
        print()
