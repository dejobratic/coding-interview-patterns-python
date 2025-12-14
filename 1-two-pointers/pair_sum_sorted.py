"""
Given a list of integers sorted in ascending order and a target value,
return the indices of any pair of numbers in the array that sum up to the
target. The order of the indices in the result doesn't matter. If no pair
is found, return an empty list.

Example 1:
  Input:  nums = [-5, -2, 3, 4, 6], target = 7
  Output: [2, 3]

Example 2:
  Input:  nums = [-2, -1, 0, 2, 3, 5], target = 2
  Output: [1, 4]
  Explanation: other valid output could be [2, 3]
"""


def pair_sum(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
