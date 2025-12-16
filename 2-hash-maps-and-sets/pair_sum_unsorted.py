"""
Given an list of integers, return the indexes of any two numbers that
add up to a target. The order of the indexes in the result doesn't 
matter. If no pair is found, return an empty list.

Example:
  Input:  nums = [-1, 3, 4, 2], target = 3
  Output: [0, 2]

Constraints:
  The same index cannot be used twice in the result.
"""


def pair_sum(nums: list[int], target: int) -> list[int]:
    index_by_num: dict[int, int] = {}

    for i, num in enumerate(nums):
        num_diff = target - num

        if num_diff in index_by_num:
            return [index_by_num[num_diff], i]

        index_by_num[num] = i

    return []
