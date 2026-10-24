# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import shortest_subarray_at_least_k  # noqa: E402
# ---- End of generated header ----

import random

class TestShortestSubarrayAtLeastK(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(shortest_subarray_at_least_k([1], 1), 1)
        self.assertEqual(shortest_subarray_at_least_k([1, 2], 4), -1)
        self.assertEqual(shortest_subarray_at_least_k([2, -1, 2], 3), 3)
        self.assertEqual(shortest_subarray_at_least_k([84, -37, 32, 40, 95], 167), 3)

    def test_single_element(self) -> None:
        self.assertEqual(shortest_subarray_at_least_k([5], 5), 1)
        self.assertEqual(shortest_subarray_at_least_k([4], 5), -1)
        self.assertEqual(shortest_subarray_at_least_k([-1], 1), -1)

    def test_all_negatives_and_zeros(self) -> None:
        self.assertEqual(shortest_subarray_at_least_k([-1, -2, -3], 1), -1)
        self.assertEqual(shortest_subarray_at_least_k([0, 0, 0], 1), -1)
        self.assertEqual(shortest_subarray_at_least_k([0, 0, 1], 1), 1)

    def test_negative_values_handling(self) -> None:
        # Subarray [7, -1, 2] sum is 8 >= 7 (len 3), but [8] is len 1
        self.assertEqual(shortest_subarray_at_least_k([7, -1, 2, 8], 8), 1)
        # [48, 99, 37, 4, -31] k = 140 -> [48, 99] = 147 (len 2)
        self.assertEqual(shortest_subarray_at_least_k([48, 99, 37, 4, -31], 140), 2)

    def test_duplicates_and_exact_sum(self) -> None:
        self.assertEqual(shortest_subarray_at_least_k([2, 2, 2, 2], 6), 3)
        self.assertEqual(shortest_subarray_at_least_k([3, 3, 3], 9), 3)

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        # 20,000 elements between -100 and 100
        nums = [rng.randint(-100, 100) for _ in range(20000)]
        # Insert a guaranteed sequence of sum 500 of length 5 at an arbitrary position
        nums[10000:10005] = [100, 100, 100, 100, 100]
        res = shortest_subarray_at_least_k(nums, 500)
        self.assertLessEqual(res, 5)
        self.assertGreater(res, 0)
