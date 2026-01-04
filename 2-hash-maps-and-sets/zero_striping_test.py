from copy import deepcopy
from zero_striping import zero_striping


def test_empty_matrix():
    # arrange
    matrix: list[list[int]] = []

    # act
    result = zero_striping(matrix)

    # assert
    assert result is None
    assert matrix == []


def test_matrix_with_empty_row():
    # arrange
    matrix: list[list[int]] = [[]]

    # act
    result = zero_striping(matrix)

    # assert
    assert result is None
    assert matrix == [[]]


def test_matrix_with_no_zeros_is_unchanged():
    # arrange
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    original = deepcopy(matrix)
    original_id = id(matrix)

    # act
    result = zero_striping(matrix)

    # assert
    assert result is None
    assert id(matrix) == original_id  # mutated in place (same object)
    assert matrix == original


def test_single_zero_sets_entire_row_and_column_to_zero():
    # arrange
    matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    # act
    zero_striping(matrix)

    # assert
    assert matrix == [
        [1, 0, 3],
        [0, 0, 0],
        [7, 0, 9],
    ]


def test_multiple_zeros_in_different_rows_and_cols():
    # arrange
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 0],
    ]

    # act
    zero_striping(matrix)

    # assert
    assert matrix == [
        [1, 0, 3, 4, 0],
        [0, 0, 0, 0, 0],
        [11, 0, 13, 14, 0],
        [0, 0, 0, 0, 0],
    ]


def test_zeros_in_first_row_and_first_col():
    # arrange
    matrix = [
        [0, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    # act
    zero_striping(matrix)

    # assert
    assert matrix == [
        [0, 0, 0],
        [0, 5, 0],
        [0, 0, 0],
    ]


def test_rectangular_matrix():
    # arrange
    matrix = [
        [1, 2, 0, 4],
        [5, 6, 7, 8],
    ]

    # act
    zero_striping(matrix)

    # assert
    assert matrix == [
        [0, 0, 0, 0],
        [5, 6, 0, 8],
    ]
