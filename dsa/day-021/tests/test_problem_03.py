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
from problem_03 import subarray_sum  # noqa: E402
# ---- End of generated header ----

import random
from collections import defaultdict


class TestSubarraySum(TestCase):
    def test_example_one(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)

    def test_example_two(self):
        self.assertEqual(subarray_sum([1, -1, 0], 0), 3)

    def test_single_element_matching(self):
        self.assertEqual(subarray_sum([5], 5), 1)

    def test_single_element_not_matching(self):
        self.assertEqual(subarray_sum([5], 3), 0)

    def test_all_zeros(self):
        # For an array of five zeros, every non-empty subarray sums to 0.
        # Number of non-empty subarrays is 5 * 6 // 2 = 15.
        nums = [0, 0, 0, 0, 0]
        self.assertEqual(subarray_sum(nums, 0), 15)

    def test_alternating_negatives_and_positives(self):
        # Subarrays summing to 0 in [1, -1, 1, -1]
        nums = [1, -1, 1, -1]
        self.assertEqual(subarray_sum(nums, 0), 4)

    def test_no_subarray_sums_to_k(self):
        nums = [2, 4, 6, 8]
        self.assertEqual(subarray_sum(nums, 5), 0)

    def test_large_input_performance_and_correctness(self):
        # 10,000 elements with deterministic sequence
        rng = random.Random(42)
        nums = [rng.randint(-5, 5) for _ in range(10000)]
        k = 0
        
        # Compute expected result using an independent mathematical prefix sum accumulation
        prefix = 0
        counts = defaultdict(int)
        counts[0] = 1
        expected = 0
        for x in nums:
            prefix += x
            expected += counts[prefix - k]
            counts[prefix] += 1
            
        self.assertEqual(subarray_sum(nums, k), expected)
