
"""
A palindrome is a sequence of characters that reads the same forwards
and backwards.

Given a string, determine if it's a palindrome after removing all
non-alphanumeric characters. A character is alphanumeric if it's either
a letter or a number.

Example 1:
  Input:  s = "a dog! a panic in a pagoda."
  Output: True

Example 2:
  Input:  s = "abc123"
  Output: False

Constraints:
  A string may include a combination of lowercase English letters,
  numbers, spaces and punctuations.
"""


def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
