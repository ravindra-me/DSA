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
from problem_01 import partition_lomuto  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestLomutoPartition(unittest.TestCase):
    def assert_valid_partition(self, nums: list[int], orig_pivot_val: int, return_idx: int):
        self.assertEqual(nums[return_idx], orig_pivot_val)
        for k in range(return_idx):
            self.assertLessEqual(nums[k], orig_pivot_val)
        for k in range(return_idx + 1, len(nums)):
            self.assertGreater(nums[k], orig_pivot_val)

    def test_example_1(self):
        nums = [3, 8, 2, 5, 1, 4]
        pivot_index = 5
        pivot_val = nums[pivot_index]
        res_idx = partition_lomuto(nums, pivot_index)
        self.assertEqual(res_idx, 3)
        self.assert_valid_partition(nums, pivot_val, res_idx)

    def test_example_2(self):
        nums = [2, 1]
        pivot_index = 0
        pivot_val = nums[pivot_index]
        res_idx = partition_lomuto(nums, pivot_index)
        self.assertEqual(res_idx, 1)
        self.assert_valid_partition(nums, pivot_val, res_idx)

    def test_single_element(self):
        nums = [42]
        pivot_index = 0
        pivot_val = nums[pivot_index]
        res_idx = partition_lomuto(nums, pivot_index)
        self.assertEqual(res_idx, 0)
        self.assertEqual(nums, [42])

    def test_duplicates_and_negatives(self):
        nums = [-3, 0, -3, 5, -1, 0, 2]
        pivot_index = 1  # pivot_val = 0
        pivot_val = nums[pivot_index]
        res_idx = partition_lomuto(nums, pivot_index)
        self.assert_valid_partition(nums, pivot_val, res_idx)

    def test_pivot_at_start(self):
        nums = [10, 1, 5, 2, 8]
        pivot_index = 0
        pivot_val = nums[pivot_index]
        res_idx = partition_lomuto(nums, pivot_index)
        self.assert_valid_partition(nums, pivot_val, res_idx)

    def test_large_input(self):
        rng = random.Random(42)
        nums = [rng.randint(-10**6, 10**6) for _ in range(10000)]
        pivot_index = 4500
        pivot_val = nums[pivot_index]
        
        res_idx = partition_lomuto(nums, pivot_index)
        self.assert_valid_partition(nums, pivot_val, res_idx)
