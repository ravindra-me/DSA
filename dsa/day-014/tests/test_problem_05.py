# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import shortest_palindrome  # noqa: E402
# ---- End of generated header ----

class TestShortestPalindrome(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(shortest_palindrome("aacecaaa"), "aaacecaaa")
        self.assertEqual(shortest_palindrome("abcd"), "dcbabcd")
        self.assertEqual(shortest_palindrome(""), "")

    def test_single_character(self) -> None:
        self.assertEqual(shortest_palindrome("a"), "a")
        self.assertEqual(shortest_palindrome("z"), "z")

    def test_already_palindrome(self) -> None:
        self.assertEqual(shortest_palindrome("racecar"), "racecar")
        self.assertEqual(shortest_palindrome("noon"), "noon")
        self.assertEqual(shortest_palindrome("aba"), "aba")

    def test_all_same_characters(self) -> None:
        self.assertEqual(shortest_palindrome("aaaaa"), "aaaaa")

    def test_worst_case_partial_match(self) -> None:
        # String starting with many 'a's ending with 'b'
        # Naive approach without KMP could take quadratic time
        s = "a" * 500 + "b"
        expected = "b" + "a" * 500 + "b"
        self.assertEqual(shortest_palindrome(s), expected)

    def test_alternating_characters(self) -> None:
        self.assertEqual(shortest_palindrome("ababab"), "bababab")

    def test_large_input(self) -> None:
        # Test with n = 40,000 to ensure O(n) performance
        # "a" * 20000 + "b" * 20000 -> longest palindromic prefix is "a"
        prefix = "a" * 20000
        suffix = "b" * 20000
        s = prefix + suffix
        # The longest palindromic prefix in 'a...ab...b' is just 'a...a' (length 20000)
        # Wait: 'a'*20000 is a palindrome! So longest palindromic prefix is 'a'*20000.
        # Prepending reversed suffix ('b'*20000) gives 'b'*20000 + 'a'*20000 + 'b'*20000
        expected = suffix[::-1] + s
        self.assertEqual(shortest_palindrome(s), expected)
