from triplet_sum import triplet_sum


def assert_triplets_equivalent(actual: list[list[int]], expected: list[list[int]]):
    assert sorted(map(sorted, actual)) == sorted(map(sorted, expected))


def test_empty_array():
    # arrange
    nums: list[int] = []

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [])


def test_array_with_one_element():
    # arrange
    nums = [1]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [])


def test_array_with_two_elements():
    # arrange
    nums = [1, 2]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [])


def test_array_with_three_elements_and_no_triplet_that_sums_up_to_zero():
    # arrange
    nums = [3, 1, 2]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [])


def test_array_with_three_elements_and_a_triplet_that_sums_up_to_zero():
    # arrange
    nums = [0, -1, 1]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [[-1, 0, 1]])


def test_array_with_more_than_three_elements_and_no_triplet_that_sums_up_to_zero():
    # arrange
    nums = [4, -1, -2, 0]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [])


def test_array_with_more_than_three_elements_and_a_triplet_that_sums_up_to_zero():
    # arrange
    nums = [1, -1, 0, -2]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [[-1, 0, 1]])


def test_array_with_more_than_three_elements_and_multiple_triplets_that_sums_up_to_zero():
    # arrange
    nums = [3, 1, -1, 0, -2]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [[-2, -1, 3], [-1, 0, 1]])


def test_array_with_more_than_three_elements_and_multiple_duplicate_triplets_that_sums_up_to_zero():
    # arrange
    nums = [3, 3, 2, 1, -1, 0, 0, -2, -3, -3]

    # act
    actual = triplet_sum(nums)

    # assert
    assert_triplets_equivalent(actual, [[-3, 0, 3], [-3, 1, 2],
                                        [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
