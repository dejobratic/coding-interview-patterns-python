from pair_sum_unsorted import pair_sum
import pytest


def create_pair_assertion(nums: list[int], target: int):
    def assert_valid(actual: list[int]) -> None:
        assert len(actual) == 2
        i, j = actual

        assert i != j
        assert 0 <= i < len(nums)
        assert 0 <= j < len(nums)
        assert nums[i] + nums[j] == target

    return assert_valid


def test_empty_array():
    # arrange
    nums: list[int] = []
    target = 10

    # act
    actual = pair_sum(nums, target)

    # assert
    assert actual == []


def test_array_with_one_element():
    # arrange
    nums = [1]
    target = 1

    # act
    actual = pair_sum(nums, target)

    # assert
    assert actual == []


def test_array_with_two_elements_without_a_pair_that_sums_up_to_target_value():
    # arrange
    nums = [2, 1]
    target = 2

    # act
    actual = pair_sum(nums, target)

    # assert
    assert actual == []


@pytest.mark.parametrize(
    "nums",
    [
        [2, 4],
        [3, 3]
    ]
)
def test_array_with_two_elements_with_a_single_pair_that_sums_up_to_target_value(nums: list[int]):
    # arrange
    target = 6

    # act
    actual = pair_sum(nums, target)

    # assert
    assert_valid = create_pair_assertion(nums, target)
    assert_valid(actual)


def test_array_with_more_than_two_elements_and_no_pair_that_sumsup_to_target_value():
    # arrange
    nums = [-1, 1, 0]
    target = 2

    # act
    actual = pair_sum(nums, target)

    # assert
    assert actual == []


def test_array_with_more_than_two_elements_and_a_single_pair_that_sum_up_to_target_value():
    # arrange
    nums = [6, -2, -5, 4, 3]
    target = 7

    # act
    actual = pair_sum(nums, target)

    # assert
    assert_valid = create_pair_assertion(nums, target)
    assert_valid(actual)


def test_array_with_more_than_two_elements_and_multiple_pairs_that_sum_up_to_target_value():
    # arrange
    nums = [0, -1, 3, -2, 5, 2]
    target = 2

    # act
    actual = pair_sum(nums, target)

    # assert
    assert_valid = create_pair_assertion(nums, target)
    assert_valid(actual)
