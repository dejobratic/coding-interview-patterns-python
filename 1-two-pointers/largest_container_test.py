from largest_container import largest_container
import pytest


class TestLargeContainers:
    def test_empty_array(self):
        # arrange
        heights: list[int] = []

        # act
        actual = largest_container(heights)

        # assert
        assert actual == 0

    def test_single_height(self):
        # arrange
        heights = [1]

        # act
        actual = largest_container(heights)

        # assert
        assert actual == 0

    @pytest.mark.parametrize(
        "heights",
        [
            [0, 0],
            [0, 1],
            [1, 0]
        ]
    )
    def test_two_heights_with_at_least_one_zero(self, heights: list[int]):
        # arrange
        # act
        actual = largest_container(heights)

        # assert
        assert actual == 0

    def test_two_non_zero_heights(self):
        # arrange
        height = [2, 3]

        # act
        actual = largest_container(height)

        # assert
        assert actual == 2

    @pytest.mark.parametrize(
        "heights, expected",
        [
            ([2, 7, 8, 3, 7, 6], 24),
            ([0, 0, 10, 5, 0], 5),
            ([5, 5, 5, 5, 5], 20)
        ]
    )
    def test_multiple_non_zero_heights(self, heights: list[int], expected: int):
        # arrange
        # act
        actual = largest_container(heights)

        # assert
        assert actual == expected
