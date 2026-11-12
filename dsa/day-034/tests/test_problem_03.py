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
from problem_03 import sort_colors  # noqa: E402
# ---- End of generated header ----

import random

class TestSortColors(TestCase):
    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_example_2(self):
        nums = [2, 0, 1]
        sort_colors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_single_element(self):
        nums = [0]
        sort_colors(nums)
        self.assertEqual(nums, [0])

    def test_all_same(self):
        nums = [1, 1, 1, 1]
        sort_colors(nums)
        self.assertEqual(nums, [1, 1, 1, 1])

    def test_already_sorted(self):
        nums = [0, 0, 1, 1, 2, 2]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_reverse_sorted(self):
        nums = [2, 2, 1, 1, 0, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_large_random(self):
        rng = random.Random(42)
        nums = [rng.choice([0, 1, 2]) for _ in range(50000)]
        expected = sorted(nums)
        sort_colors(nums)
        self.assertEqual(nums, expected)
