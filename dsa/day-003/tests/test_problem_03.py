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
from problem_03 import compress_string  # noqa: E402
# ---- End of generated header ----

import random

class TestStringCompression(TestCase):
    def test_example_1_multiple_groups(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        new_len = compress_string(chars)
        self.assertEqual(new_len, 6)
        self.assertEqual(chars[:new_len], ["a", "2", "b", "2", "c", "3"])

    def test_example_2_single_character(self):
        chars = ["a"]
        new_len = compress_string(chars)
        self.assertEqual(new_len, 1)
        self.assertEqual(chars[:new_len], ["a"])

    def test_example_3_multi_digit_count(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        new_len = compress_string(chars)
        self.assertEqual(new_len, 4)
        self.assertEqual(chars[:new_len], ["a", "b", "1", "2"])

    def test_all_unique_characters(self):
        chars = ["a", "b", "c", "d", "e"]
        new_len = compress_string(chars)
        self.assertEqual(new_len, 5)
        self.assertEqual(chars[:new_len], ["a", "b", "c", "d", "e"])

    def test_alternating_characters(self):
        chars = ["a", "b", "a", "b", "a"]
        new_len = compress_string(chars)
        self.assertEqual(new_len, 5)
        self.assertEqual(chars[:new_len], ["a", "b", "a", "b", "a"])

    def test_special_characters_and_digits(self):
        chars = ["#", "#", "#", "1", "1", " ", " "]
        new_len = compress_string(chars)
        self.assertEqual(new_len, 6)
        self.assertEqual(chars[:new_len], ["#", "3", "1", "2", " ", "2"])

    def test_large_input_compression(self):
        # 2000 characters with guaranteed distinct consecutive runs
        rng = random.Random(42)
        chars = []
        expected_prefix = []
        alphabet = ["x", "y", "z", "w"]
        last_char = None

        while len(chars) < 2000:
            candidates = [c for c in alphabet if c != last_char]
            c = rng.choice(candidates)
            last_char = c
            run_len = min(rng.randint(1, 50), 2000 - len(chars))
            chars.extend([c] * run_len)
            expected_prefix.append(c)
            if run_len > 1:
                expected_prefix.extend(list(str(run_len)))

        expected_len = len(expected_prefix)
        new_len = compress_string(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_prefix)
