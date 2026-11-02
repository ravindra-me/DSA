# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import length_of_longest_substring  # noqa: E402
# ---- End of generated header ----

import random

class TestLengthOfLongestSubstring(TestCase):
    def test_example_1(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(length_of_longest_substring(""), 0)

    def test_example_3(self):
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    def test_single_character(self):
        self.assertEqual(length_of_longest_substring("a"), 1)

    def test_all_unique(self):
        self.assertEqual(length_of_longest_substring("abcdefg"), 7)

    def test_substring_with_spaces_and_symbols(self):
        self.assertEqual(length_of_longest_substring("a b!c a b!c"), 5)  # "b!c a" or "!c a "

    def test_repeating_pattern(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_large_input_performance(self):
        # Large string with periodic repetition to test linear performance
        rng = random.Random(42)
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        chunk = "".join(rng.sample(alphabet, len(alphabet)))
        large_s = chunk * 2000  # length 72,000
        
        self.assertEqual(length_of_longest_substring(large_s), len(alphabet))
