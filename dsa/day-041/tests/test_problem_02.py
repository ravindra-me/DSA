# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import stable_zero_partition  # noqa: E402
# ---- End of generated header ----

import random

class TestStableZeroPartition(TestCase):
    def test_example_1(self):
        nums = [0, 1, 0, 3, 12]
        count = stable_zero_partition(nums)
        self.assertEqual(count, 3)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example_2(self):
        nums = [0, 0, 0]
        count = stable_zero_partition(nums)
        self.assertEqual(count, 0)
        self.assertEqual(nums, [0, 0, 0])

    def test_single_element_zero(self):
        nums = [0]
        count = stable_zero_partition(nums)
        self.assertEqual(count, 0)
        self.assertEqual(nums, [0])

    def test_single_element_nonzero(self):
        nums = [-42]
        count = stable_zero_partition(nums)
        self.assertEqual(count, 1)
        self.assertEqual(nums, [-42])

    def test_all_nonzero(self):
        nums = [4, -1, 7, 2]
        count = stable_zero_partition(nums)
        self.assertEqual(count, 4)
        self.assertEqual(nums, [4, -1, 7, 2])

    def test_alternating_and_negatives(self):
        nums = [0, -5, 0, 10, 0, -20, 0]
        count = stable_zero_partition(nums)
        self.assertEqual(count, 3)
        self.assertEqual(nums, [-5, 10, -20, 0, 0, 0, 0])

    def test_large_input_performance(self):
        rng = random.Random(42)
        n = 100_000
        # Generate deterministic array of mixed zeros and non-zeros
        raw_data = [rng.choice([0, rng.randint(-10**9, 10**9)]) for _ in range(n)]
        nums = list(raw_data)
        
        # Reference calculation
        expected_non_zeros = [x for x in raw_data if x != 0]
        expected_count = len(expected_non_zeros)
        expected_nums = expected_non_zeros + [0] * (n - expected_count)
        
        count = stable_zero_partition(nums)
        self.assertEqual(count, expected_count)
        self.assertEqual(nums, expected_nums)
