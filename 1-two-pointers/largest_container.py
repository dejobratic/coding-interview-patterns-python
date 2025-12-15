"""
You are given an array of numbers, each representing the height of a
vertical line on a graph. A container can be formed with any pair of
these lines, along with the x-axis of the graph. Return the amount of
water which the largest container can hold.

Example:
      
    8 |        |     
    7 |     |  |     |
    6 |     |~~|~~~~~|~~|
    5 |     |~~|~~~~~|~~|
    4 |     |~~|~~~~~|~~|
    3 |     |~~|~~|~~|~~|
    2 |  |  |~~|~~|~~|~~|
    1 |  |  |~~|~~|~~|~~|
    0 +--+--+--+--+--+--+-->
         0  1  2  3  4  5

  Input:  heights =  [2, 7, 8, 3, 7, 6]
  Output: 24
"""


def largest_container(heights: list[int]) -> int:
    result = 0
    left, right = 0, len(heights) - 1

    while left < right:
        result = max(result, _calculate(heights, left, right))

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return result


def _calculate(heights: list[int], left: int, right: int) -> int:
    return min(heights[left], heights[right]) * (right - left)
