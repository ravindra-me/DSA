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
from problem_03 import split_array  # noqa: E402
# ---- End of generated header ----

import random


class TestSplitArray(TestCase):
    def test_example_one(self) -> None:
        self.assertEqual(split_array([7, 2, 5, 10, 8], 2), 18)

    def test_example_two(self) -> None:
        self.assertEqual(split_array([1, 4, 4], 3), 4)

    def test_single_element(self) -> None:
        self.assertEqual(split_array([42], 1), 42)

    def test_k_equals_length(self) -> None:
        nums = [10, 20, 30, 5, 15]
        self.assertEqual(split_array(nums, len(nums)), 30)

    def test_k_equals_one(self) -> None:
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(split_array(nums, 1), sum(nums))

    def test_all_zeros(self) -> None:
        nums = [0, 0, 0, 0]
        self.assertEqual(split_array(nums, 2), 0)

    def test_duplicates_and_uniform_values(self) -> None:
        nums = [5, 5, 5, 5, 5, 5]
        # 6 elements split into 3 subarrays -> pairs of 2 elements each sum to 10
        self.assertEqual(split_array(nums, 3), 10)

    def test_large_input_performance(self) -> None:
        # 100,000 elements with uniform values where expected answer is known analytically
        n = 100_000
        k = 10
        nums = [2] * n
        # Splitting n elements of value 2 into k equal parts gives n // k = 10,000 elements each
        # Each subarray sum = 10,000 * 2 = 20,000
        self.assertEqual(split_array(nums, k), 20000)

    def test_large_values_with_known_splits(self) -> None:
        rng = random.Random(1337)
        chunk_size = 500
        k = 4
        nums = [rng.randint(1, 100) for _ in range(chunk_size * k)]
        # Ensure the function completes swiftly with large random elements
        ans = split_array(nums, k)
        self.assertGreaterEqual(ans, max(nums))
        self.assertLessEqual(ans, sum(nums))
