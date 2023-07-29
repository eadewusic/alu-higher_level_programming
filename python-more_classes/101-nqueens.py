#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at the given row and column is safe.
    A queen is safe if it does not attack any other queen on the board.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, row=0, board=[]):
    """
    Recursive function to solve the N queens problem using backtracking.

    Args:
        N (int):
        The size of the chessboard and the number of queens to be placed.
        row (int):
        Current row being considered.
        board (list):
        List representing the positions of queens on the board.

    Prints:
        Prints every possible solution to the N queens problem,
        one solution per line.
        Each solution is represented as a list of
        (row, column) positions for the queens.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(N, row + 1, board)
            board.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
