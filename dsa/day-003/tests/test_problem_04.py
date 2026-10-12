# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import longest_palindrome  # noqa: E402
# ---- End of generated header ----

class TestLongestPalindrome(TestCase):
    def test_example_1_tie_returns_first(self) -> None:
        # "babad" has both "bab" and "aba", but "bab" appears first
        self.assertEqual(longest_palindrome("babad"), "bab")

    def test_example_2_even_length(self) -> None:
        self.assertEqual(longest_palindrome("cbbd"), "bb")

    def test_single_character(self) -> None:
        self.assertEqual(longest_palindrome("a"), "a")

    def test_all_distinct_characters(self) -> None:
        # No palindrome of length > 1, should return the first character
        self.assertEqual(longest_palindrome("abcdef"), "a")

    def test_all_same_characters(self) -> None:
        self.assertEqual(longest_palindrome("aaaaa"), "aaaaa")

    def test_entire_string_is_palindrome(self) -> None:
        self.assertEqual(longest_palindrome("racecar"), "racecar")

    def test_case_sensitivity(self) -> None:
        # 'A' != 'a', so longest should be single character 'A'
        self.assertEqual(longest_palindrome("Aa"), "A")

    def test_large_input_palindrome_at_center(self) -> None:
        # Construct a large string (1000 chars) with unique ends and a known palindrome
        # A naive O(n^3) string-slice checker could take seconds, O(n^2) runs in ~10ms
        prefix = "abcdefghij" * 40  # 400 chars
        middle = "x" * 200          # 200 chars
        suffix = "klmnopqrst" * 40  # 400 chars
        s = prefix + middle + suffix
        self.assertEqual(longest_palindrome(s), middle)
