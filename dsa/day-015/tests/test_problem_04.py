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
from problem_04 import longest_subarray_with_limit  # noqa: E402
# ---- End of generated header ----

import random


class TestLongestSubarrayWithLimit(TestCase):
    def test_examples(self):
        self.assertEqual(longest_subarray_with_limit([8, 2, 4, 7], 4), 2)
        self.assertEqual(longest_subarray_with_limit([10, 1, 2, 4, 7, 2], 5), 4)
        self.assertEqual(longest_subarray_with_limit([4, 2, 2, 2, 4, 4, 2, 2], 0), 3)

    def test_empty_and_single_element(self):
        self.assertEqual(longest_subarray_with_limit([], 5), 0)
        self.assertEqual(longest_subarray_with_limit([42], 0), 1)
        self.assertEqual(longest_subarray_with_limit([100], 10), 1)

    def test_zero_limit(self):
        nums = [1, 1, 2, 2, 2, 2, 3, 3, 2, 2]
        self.assertEqual(longest_subarray_with_limit(nums, 0), 4)

    def test_entire_array_valid(self):
        nums = [5, 6, 7, 6, 5, 4, 5]
        # min=4, max=7, diff=3 <= 3
        self.assertEqual(longest_subarray_with_limit(nums, 3), 7)

    def test_strictly_increasing_and_decreasing(self):
        inc = [1, 2, 3, 4, 5, 6]
        self.assertEqual(longest_subarray_with_limit(inc, 2), 3)
        dec = [6, 5, 4, 3, 2, 1]
        self.assertEqual(longest_subarray_with_limit(dec, 1), 2)

    def test_alternating_extremes(self):
        nums = [1, 10, 1, 10, 1, 10]
        self.assertEqual(longest_subarray_with_limit(nums, 8), 1)
        self.assertEqual(longest_subarray_with_limit(nums, 9), 6)

    def test_large_input_performance(self):
        # 50,000 elements with known step increments
        # An O(N^2) approach would time out, O(N) finishes well under 0.2s
        rng = random.Random(1337)
        nums = [rng.randint(1, 100) for _ in range(50000)]
        limit = 10
        result = longest_subarray_with_limit(nums, limit)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 50000)
