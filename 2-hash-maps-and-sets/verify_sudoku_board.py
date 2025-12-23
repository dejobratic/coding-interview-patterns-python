"""
Given a partially completed 9x9 Sudoku board, determine if the current
state of the board adheres to the rules of the game:

- Each row and column must contain unique numbers between 1 and 9, or
  be empty (represented as 0).
- Each of the nine 3x3 subgrids that compose the grid must contain
  unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the current state of the board
is valid given these rules, not whether the board is solvable.

Example:
  Input:
    +-------+-------+-------+
    | 3 . 6 | . 5 8 | 4 . . |
    | 5 2 . | . . . | . . . |
    | . 8 7 | . . . | . 3 1 |
    +-------+-------+-------+
    | 1 . 2 | 5 . . | 3 2 . |
    | 9 . . | 8 6 3 | . . 5 |
    | . 5 . | . 9 . | 6 . . |
    +-------+-------+-------+
    | . 3 . | . . 8 | 2 5 . |
    | . 1 . | . . . | . 7 4 |
    | . . 2 | 2 . 6 | . . . |
    +-------+-------+-------+
  Output:  False
"""

Board = list[list[int]]

board_size: int = 9
grid_size: int = 3


def verify_sudoku_board(board: Board) -> bool:
    row_sets: list[set[int]] = [set() for _ in range(board_size)]
    col_sets: list[set[int]] = [set() for _ in range(board_size)]
    grid_sets: list[set[int]] = [set() for _ in range(board_size)]

    for row in range(board_size):
        for col in range(board_size):
            el = board[row][col]
            if el == 0:
                continue

            grid = (row // grid_size) * grid_size + (col // grid_size)

            if el in row_sets[row] or el in col_sets[col] or el in grid_sets[grid]:
                return False

            row_sets[row].add(el)
            col_sets[col].add(el)
            grid_sets[grid].add(el)

    return True
