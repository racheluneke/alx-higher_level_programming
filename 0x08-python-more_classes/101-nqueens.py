#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for _ in range(n)]
    [row.append(' ') for _ in range(n) for row in board]
    return board


def copy_board(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return board


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_unavail_spots(board, row, col):
    """Mark spots on a chessboard as unavailable.

    All spots where non-attacking queens can no
    longer be placed are marked as 'x'.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Mark all forward spots as 'x'
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all backward spots as 'x'
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all spots below as 'x'
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all spots above as 'x'
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all spots diagonally down to the right as 'x'
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all spots diagonally up to the left as 'x'
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Mark all spots diagonally up to the right as 'x'
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all spots diagonally down to the left as 'x'
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_nqueens(board, row, queens, solu):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solu (list): A list of lists of solutions.
    Returns:
        solu
    """
    if queens == len(board):
        solu.append(get_solution(board))
        return solu

    for col in range(len(board)):
        if board[row][col] == " ":
            t_board = copy_board(board)
            t_board[row][col] = "Q"
            mark_unavail_spots(t_board, row, col)
            solu = solve_nqueens(t_board, row + 1, queens + 1, solu)

    return solu


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = init_board(int(sys.argv[1]))
    solution_set = solve_nqueens(chessboard, 0, 0, [])
    for solution in solution_set:
        print(solution)
