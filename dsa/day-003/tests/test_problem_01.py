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
from problem_01 import is_palindrome  # noqa: E402
# ---- End of generated header ----

class TestValidPalindrome(TestCase):
    def test_example_1_classic_phrase(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_example_2_non_palindrome(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_example_3_only_punctuation_and_spaces(self):
        self.assertTrue(is_palindrome("   .,:;!?   "))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
        self.assertTrue(is_palindrome("7"))
        self.assertTrue(is_palindrome("!"))

    def test_mixed_alphanumeric_mismatch(self):
        self.assertFalse(is_palindrome("0P"))
        self.assertFalse(is_palindrome("ab2a"))

    def test_even_and_odd_length_palindromes(self):
        self.assertTrue(is_palindrome("AbBa"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1221"))

    def test_large_input_performance(self):
        half = "AbcDef12345" * 9000
        palindrome_str = half + "x" + half[::-1]
        self.assertTrue(is_palindrome(palindrome_str))

        non_palindrome_str = half + "x" + half[::-1] + "z"
        self.assertFalse(is_palindrome(non_palindrome_str))
