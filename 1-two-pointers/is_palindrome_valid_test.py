from is_palindrome_valid import is_palindrome_valid
import pytest


class TestIsPalindromeValid:
    def test_empty_string(self):
        # arrange
        s = ""

        # act
        actual = is_palindrome_valid(s)

        # assert
        assert actual == True

    def test_single_character_string(self):
        # arrange
        s = "a"

        # act
        actual = is_palindrome_valid(s)

        # assert
        assert actual == True

    def test_two_character_non_palindromic_string(self):
        # arrange
        s = "ab"

        # act
        actual = is_palindrome_valid(s)

        # assert
        assert actual == False

    def test_two_character_palindromic_string(self):
        # arrange
        s = "aa"

        # act
        actual = is_palindrome_valid(s)

        # assert
        assert actual == True

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abc123", False),
            ("#$%^a&*b()", False),
        ],
    )
    def test_multiple_character_non_palindromic_string(self, s: str, expected: bool):
        # arrange
        # act
        actual = is_palindrome_valid(s)

        # assert
        assert actual == False

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("!@#$%^&*()", True),
            ("20.02.2002", True),
            ("a dog! a panic in a pagoda.", True),
        ],
    )
    def test_multiple_character_palindromic_string(self, s: str, expected: bool):
        # arrange
        # act
        actual = is_palindrome_valid(s)

        # assert
        assert actual == expected
