from typing import List

def binary_search(nums: List[int], target: int):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    nums = [1, 2, 4, 5, 7, 8, 9]

    for target in [0, 4, 6, 10]:
        print(f'Insertion index of {target} is {binary_search(nums, target)}')
