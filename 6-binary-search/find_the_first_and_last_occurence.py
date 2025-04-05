from typing import List

def binary_search_lower_bound(nums: List[int], target: int):
    left, right =  0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left if nums and nums[left] == target else -1

def binary_search_upper_bound(nums: List[int], target: int):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid
    
    return right if nums and nums[right] == target else -1

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]

    for target in [0, 4, 5, 12]:
        lower = binary_search_lower_bound(nums, target)
        upper = binary_search_upper_bound(nums, target)
        print(f'{target} -> [{lower}, {upper}]')
