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
from problem_03 import longest_duplicate_substring_length  # noqa: E402
# ---- End of generated header ----

import random

class TestLongestDuplicateSubstringLength(TestCase):
    def test_example_banana(self):
        self.assertEqual(longest_duplicate_substring_length("banana"), 3)

    def test_example_no_duplicates(self):
        self.assertEqual(longest_duplicate_substring_length("abcd"), 0)

    def test_all_identical_characters(self):
        # In "aaaaa", "aaaa" appears at index 0 and 1 -> length 4
        self.assertEqual(longest_duplicate_substring_length("aaaaa"), 4)

    def test_minimum_length_inputs(self):
        self.assertEqual(longest_duplicate_substring_length("ab"), 0)
        self.assertEqual(longest_duplicate_substring_length("aa"), 1)

    def test_overlapping_repetitions(self):
        # "ababab": "abab" appears at index 0 and index 2 (length 4)
        self.assertEqual(longest_duplicate_substring_length("ababab"), 4)

    def test_distinct_with_single_repeated_pair(self):
        s = "abcdefgxyzabcdefg"
        # "abcdefg" is duplicated (length 7)
        self.assertEqual(longest_duplicate_substring_length(s), 7)

    def test_large_input_performance(self):
        rng = random.Random(42)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        # Construct unique-ish string of length ~10000, then inject a known duplicate
        base_chars = [alphabet[rng.randint(0, 25)] for _ in range(10000)]
        target_len = 150
        secret = ["z"] * target_len
        # Place at index 1000 and index 6000
        base_chars[1000:1000 + target_len] = secret
        base_chars[6000:6000 + target_len] = secret
        s = "".join(base_chars)
        result = longest_duplicate_substring_length(s)
        self.assertGreaterEqual(result, target_len)
