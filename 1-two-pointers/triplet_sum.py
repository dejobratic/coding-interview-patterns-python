"""
Given a list of integers, return all triplets [a, b, c] such that
a + b + c = 0. The solution must not contain duplicate triplets (e.g
[1, 2, 3] and [2, 3, 1] are considered duplicate triplets). If no such
triplets are found, return an empty list.

Each triplet can be arranged in any order, and the output can be returned
in any order.

Example:
  Input:  nums = [0, -1, 2, -3, 1]
  Output: [[-3, 1, 2], [-1, 0, 1]]
"""
from typing import Iterator


def triplet_sum(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    nums = sorted(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] > 0:
            break

        result.extend(_triplet_sum(nums, i))

    return result


def _triplet_sum(nums: list[int], current_index: int) -> Iterator[list[int]]:
    left, right = current_index + 1, len(nums) - 1

    while left < right:
        current_sum = nums[current_index] + nums[left] + nums[right]

        if current_sum == 0:
            yield [nums[current_index], nums[left], nums[right]]
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif current_sum < 0:
            left += 1
        else:
            right -= 1
