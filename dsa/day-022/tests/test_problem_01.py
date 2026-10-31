# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_01 import is_valid_palindrome  # noqa: E402
# ---- End of generated header ----

class TestValidPalindrome(TestCase):
    def test_example_1(self) -> None:
        self.assertTrue(is_valid_palindrome("A man, a plan, a canal: Panama"))

    def test_example_2(self) -> None:
        self.assertFalse(is_valid_palindrome("race a car"))

    def test_example_3_non_alphanumeric_only(self) -> None:
        self.assertTrue(is_valid_palindrome(" ., "))

    def test_single_character(self) -> None:
        self.assertTrue(is_valid_palindrome("a"))
        self.assertTrue(is_valid_palindrome("!"))

    def test_alphanumeric_digits_and_letters_mismatch(self) -> None:
        # '0' and 'P' are both alphanumeric, but not matching
        self.assertFalse(is_valid_palindrome("0P"))

    def test_palindrome_with_numbers(self) -> None:
        self.assertTrue(is_valid_palindrome("12321"))
        self.assertTrue(is_valid_palindrome("1b2: 2b1"))
        self.assertTrue(is_valid_palindrome("No 'x' in Nixon!"))
        self.assertFalse(is_valid_palindrome("123421"))

    def test_large_input_palindrome(self) -> None:
        # 200,000 characters: half 'a', interspersed punctuation, mirrored
        half = "a!b@c#" * 16666  # ~100k chars
        full = half + half[::-1]
        self.assertTrue(is_valid_palindrome(full))

    def test_large_input_non_palindrome(self) -> None:
        half = "a!b@c#" * 16666
        full_modified = half + "de" + half[::-1]
        self.assertFalse(is_valid_palindrome(full_modified))
