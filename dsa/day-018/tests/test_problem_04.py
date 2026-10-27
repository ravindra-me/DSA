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
from problem_04 import longest_consecutive  # noqa: E402
# ---- End of generated header ----

import random

class TestLongestConsecutive(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_example_2(self):
        self.assertEqual(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_empty_input(self):
        self.assertEqual(longest_consecutive([]), 0)

    def test_single_element(self):
        self.assertEqual(longest_consecutive([10]), 1)

    def test_duplicates_and_negatives(self):
        self.assertEqual(longest_consecutive([-1, -2, -3, 0, -2, 1, 2]), 6)

    def test_no_consecutive_elements(self):
        self.assertEqual(longest_consecutive([10, 30, 20, 40]), 1)

    def test_large_input_performance(self):
        rng = random.Random(42)
        # Create a large sequence of 50,000 continuous integers shuffled with noise
        base = list(range(-25000, 25000))
        noise = [rng.randint(100000, 200000) for _ in range(10000)]
        full_list = base + noise
        rng.shuffle(full_list)
        self.assertEqual(longest_consecutive(full_list), 50000)
