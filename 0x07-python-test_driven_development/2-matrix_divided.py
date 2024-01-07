#!/usr/bin/python3
"""function to divide matrix"""


def matrix_divided(matrix, divisor):
    """
Function to divide a matrix by a given divisor.

Parameters:
- matrix (list of lists): The matrix to be divided.
Each element of the matrix should be an integer or a float.
- divisor (int or float): The number by which the matrix will be divided.

Returns:
- new_matrix (list of lists): The resulting matrix after division.
Each element of the new matrix will be rounded to 2 decimal places.

Raises:
- TypeError: If the matrix is not a valid matrix (list of lists)
 of integers/floats, or if each row of the matrix
 does not have the same size, or if the divisor is not a number.
- ZeroDivisionError: If the divisor is zero.
"""

    num_columns = len(matrix[0])

    if any(not isinstance(elm, (int, float)) for row in matrix for elm in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if any(len(row) != num_columns for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(divisor) not in (int, float):
        raise TypeError("div must be a number")
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elm / divisor, 2) for elm in row] for row in matrix]

    return new_matrix
