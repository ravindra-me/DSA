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
from problem_01 import NumArray  # noqa: E402
# ---- End of generated header ----

import random


class TestNumArray(TestCase):
    def test_example_1(self) -> None:
        nums = [-2, 0, 3, -5, 2, -1]
        na = NumArray(nums)
        self.assertEqual(na.sum_range(0, 2), 1)
        self.assertEqual(na.sum_range(2, 5), -1)
        self.assertEqual(na.sum_range(0, 5), -3)

    def test_single_element(self) -> None:
        na = NumArray([5])
        self.assertEqual(na.sum_range(0, 0), 5)

    def test_single_element_negative(self) -> None:
        na = NumArray([-42])
        self.assertEqual(na.sum_range(0, 0), -42)

    def test_all_zeros(self) -> None:
        na = NumArray([0, 0, 0, 0, 0])
        self.assertEqual(na.sum_range(1, 3), 0)
        self.assertEqual(na.sum_range(0, 4), 0)

    def test_all_identical_elements(self) -> None:
        na = NumArray([7, 7, 7, 7])
        self.assertEqual(na.sum_range(0, 3), 28)
        self.assertEqual(na.sum_range(1, 2), 14)
        self.assertEqual(na.sum_range(2, 2), 7)

    def test_alternating_signs(self) -> None:
        nums = [1, -1, 1, -1, 1, -1]
        na = NumArray(nums)
        self.assertEqual(na.sum_range(0, 1), 0)
        self.assertEqual(na.sum_range(0, 5), 0)
        self.assertEqual(na.sum_range(1, 4), 0)
        self.assertEqual(na.sum_range(1, 3), -1)
        self.assertEqual(na.sum_range(2, 4), 1)

    def test_boundary_queries(self) -> None:
        nums = [10, 20, 30, 40, 50]
        na = NumArray(nums)
        # First element
        self.assertEqual(na.sum_range(0, 0), 10)
        # Last element
        self.assertEqual(na.sum_range(4, 4), 50)
        # Entire array
        self.assertEqual(na.sum_range(0, 4), 150)

    def test_large_number_of_queries(self) -> None:
        rng = random.Random(42)
        n = 50_000
        nums = [rng.randint(-1000, 1000) for _ in range(n)]
        na = NumArray(nums)

        # Precompute reference array for verification
        ref_prefix = [0] * (n + 1)
        for i, val in enumerate(nums):
            ref_prefix[i + 1] = ref_prefix[i] + val

        # Perform 20,000 queries to ensure O(1) performance
        for _ in range(20_000):
            l = rng.randint(0, n - 1)
            r = rng.randint(l, n - 1)
            expected = ref_prefix[r + 1] - ref_prefix[l]
            self.assertEqual(na.sum_range(l, r), expected)
