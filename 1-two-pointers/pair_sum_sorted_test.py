from pair_sum_sorted import pair_sum


class TestPairSum:
    def test_empty_array(self):
        # arrange
        nums: list[int] = []
        target = 10

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == []

    def test_array_with_one_element(self):
        # arrange
        nums = [1]
        target = 1

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == []

    def test_array_with_two_elements_without_a_pair_that_sums_up_to_target_value(self):
        # arrange
        nums = [1, 2]
        target = 2

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == []

    def test_array_with_two_elements_with_a_pair_that_sums_up_to_target_value(self):
        # arrange
        nums = [1, 2]
        target = 3

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == [0, 1]

    def test_array_with_more_than_two_elements_and_no_pair_that_sumsup_to_target_value(self):
        # arrange
        nums = [-1, 0, 1]
        target = 2

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == []

    def test_array_with_more_than_two_elements_and_a_single_pair_that_sum_up_to_target_value(self):
        # arrange
        nums = [-5, -2, 3, 4, 6]
        target = 7

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == [2, 3]

    def test_array_with_more_than_two_elements_and_multiple_pairs_that_sum_up_to_target_value(self):
        # arrange
        nums = [-2, -1, 0, 2, 3, 5]
        target = 2

        # act
        actual = pair_sum(nums, target)

        # assert
        assert actual == [1, 4]
