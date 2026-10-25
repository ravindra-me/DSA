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
from problem_03 import longest_consecutive_sequence  # noqa: E402
# ---- End of generated header ----

import random


class TestLongestConsecutiveSequence(TestCase):
    def test_examples(self):
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
        self.assertEqual(longest_consecutive_sequence([]), 0)

    def test_single_element(self):
        self.assertEqual(longest_consecutive_sequence([42]), 1)
        self.assertEqual(longest_consecutive_sequence([-10]), 1)

    def test_duplicates(self):
        self.assertEqual(longest_consecutive_sequence([1, 2, 0, 1]), 3)
        self.assertEqual(longest_consecutive_sequence([5, 5, 5, 5]), 1)
        self.assertEqual(longest_consecutive_sequence([1, 2, 2, 3, 3, 4, 4]), 4)

    def test_negative_numbers_and_zero(self):
        self.assertEqual(longest_consecutive_sequence([-5, -4, -3, -2, -1, 0, 1]), 7)
        self.assertEqual(longest_consecutive_sequence([-10, -20, -30]), 1)
        self.assertEqual(longest_consecutive_sequence([-1, -2, -3, 100, 101]), 3)

    def test_no_consecutive_elements(self):
        self.assertEqual(longest_consecutive_sequence([10, 30, 50, 70]), 1)
        self.assertEqual(longest_consecutive_sequence([-100, 0, 100]), 1)

    def test_large_input_performance(self):
        # Large input: 50,000 elements partitioned into chunks
        # Consecutive sequence of 25,000 elements plus scattered elements
        rng = random.Random(42)
        consecutive_part = list(range(100_000, 125_000))
        scattered_part = [rng.randint(1_000_000, 2_000_000) for _ in range(25_000)]
        full_list = consecutive_part + scattered_part
        rng.shuffle(full_list)

        # The longest consecutive sequence is guaranteed to be at least 25000
        result = longest_consecutive_sequence(full_list)
        self.assertGreaterEqual(result, 25_000)
