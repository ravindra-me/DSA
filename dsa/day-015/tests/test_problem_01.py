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
from problem_01 import is_deque_palindrome  # noqa: E402
# ---- End of generated header ----

import random
from collections import deque


class TestValidateDequePalindrome(TestCase):
    def test_example_1_classic_phrase(self):
        self.assertTrue(is_deque_palindrome("A man, a plan, a canal: Panama"))

    def test_example_2_non_palindrome(self):
        self.assertFalse(is_deque_palindrome("race a car"))

    def test_example_3_symbols_only(self):
        self.assertTrue(is_deque_palindrome(".,"))

    def test_single_character(self):
        self.assertTrue(is_deque_palindrome("x"))
        self.assertTrue(is_deque_palindrome(" 	 ? x ! "))

    def test_even_length_palindromes(self):
        self.assertTrue(is_deque_palindrome("Abba"))
        self.assertTrue(is_deque_palindrome("1221"))
        self.assertFalse(is_deque_palindrome("1231"))

    def test_numeric_and_mixed(self):
        self.assertTrue(is_deque_palindrome("0P0"))
        self.assertFalse(is_deque_palindrome("0P"))

    def test_large_input_palindrome(self):
        rng = random.Random(42)
        chars = [rng.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(50_000)]
        palindrome_core = chars + chars[::-1]
        # Interleave with punctuation
        noisy = []
        for ch in palindrome_core:
            noisy.append(ch)
            noisy.append(", ")
        full_str = "".join(noisy)
        self.assertTrue(is_deque_palindrome(full_str))

    def test_large_input_non_palindrome(self):
        rng = random.Random(1337)
        chars = [rng.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(50_000)]
        half1 = chars
        half2 = chars[::-1]
        # Introduce mismatch in the middle
        half1[-1] = "a" if half1[-1] != "a" else "b"
        full_str = "".join(half1 + half2)
        self.assertFalse(is_deque_palindrome(full_str))
