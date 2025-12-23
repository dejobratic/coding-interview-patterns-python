"""
For each zero in an m x n matrix, set its entire row and column to zero
in place.

Example:

Example:
  Input:
        0   1   2   3   4
      +---+---+---+---+---+
    0 | 1 | 2 | 3 | 4 | 5 |
      +---+---+---+---+---+
    1 | 6 | 0 | 8 | 9 |10 |
      +---+---+---+---+---+
    2 |11 |12 |13 |14 |15 |
      +---+---+---+---+---+
    3 |16 |17 |18 |19 | 0 |
      +---+---+---+---+---+

  Output:
        0   1   2   3   4
      +---+---+---+---+---+
    0 | 1 | 0 | 3 | 4 | 0 |
      +---+---+---+---+---+
    1 | 0 | 0 | 0 | 0 | 0 |
      +---+---+---+---+---+
    2 |11 | 0 |13 |14 | 0 |
      +---+---+---+---+---+
    3 | 0 | 0 | 0 | 0 | 0 |
      +---+---+---+---+---+
"""


def zero_striping(matrix: list[list[int]]):
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    zero_rows: set[int] = set()
    zero_cols: set[int] = set()

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    for row in zero_rows:
        for col in range(n):
            matrix[row][col] = 0

    for row in range(m):
        for col in zero_cols:
            matrix[row][col] = 0


def zero_striping_in_place(matrix: list[list[int]]):
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_has_zero, first_col_has_zero = False, False

    for col in range(n):
        if matrix[0][col] == 0:
            first_row_has_zero = True
            break

    for row in range(m):
        if matrix[row][0] == 0:
            first_col_has_zero = True
            break

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if first_row_has_zero:
        for col in range(n):
            matrix[0][col] = 0

    if first_col_has_zero:
        for row in range(m):
            matrix[row][0] = 0
