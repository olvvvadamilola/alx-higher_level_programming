#!/usr/bin/python3
""" Solves the N queens problem"""
import sys


def is_safe(board, row, col, N):
    """ Checks if a queen can be placed on the board
    at the given row and column

    Args:
        board (list): The board
        row (int): The row
        column (int): The column
        N (int): The size of the board

    Returns:
        bool: True if the queen can be placed
             False if the queen can't be placed
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_util(board, 0, N)


def solve_util(board, col, N):
    if col == N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_util(board, col + 1, N) or res
            board[i][col] = 0

    return res


def print_solution(board, N):
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_n_queens(sys.argv[1])
