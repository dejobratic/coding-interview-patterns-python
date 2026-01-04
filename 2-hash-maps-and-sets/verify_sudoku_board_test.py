from verify_sudoku_board import verify_sudoku_board, Board


def test_empty_board_is_valid():
    # arrange
    board: Board = [[0] * 9 for _ in range(9)]

    # act
    actual = verify_sudoku_board(board)

    # assert
    assert actual is True


def test_valid_partially_filled_board_is_valid():
    # arrange
    board: Board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    # act
    actual = verify_sudoku_board(board)

    # assert
    assert actual is True


def test_duplicate_in_a_row_is_invalid():
    # arrange
    board: Board = [[0] * 9 for _ in range(9)]
    board[0][0] = 5
    board[0][8] = 5

    # act
    actual = verify_sudoku_board(board)

    # assert
    assert actual is False


def test_duplicate_in_a_column_is_invalid():
    # arrange
    board: Board = [[0] * 9 for _ in range(9)]
    board[1][3] = 7
    board[8][3] = 7

    # act
    actual = verify_sudoku_board(board)

    # assert
    assert actual is False


def test_duplicate_in_a_3x3_grid_is_invalid():
    # arrange
    board: Board = [[0] * 9 for _ in range(9)]
    board[0][0] = 9
    board[2][2] = 9

    # act
    actual = verify_sudoku_board(board)

    # assert
    assert actual is False


def test_given_example_board_is_invalid():
    # arrange
    board: Board = [
        [3, 0, 6, 0, 5, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [1, 0, 2, 5, 0, 0, 3, 2, 0],  # <- row has two 2s (col 2 and col 7)
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [0, 3, 0, 0, 0, 8, 2, 5, 0],
        [0, 1, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 2, 2, 0, 6, 0, 0, 0],  # <- row has two 2s (col 2 and col 3)
    ]

    # act
    actual = verify_sudoku_board(board)

    # assert
    assert actual is False
