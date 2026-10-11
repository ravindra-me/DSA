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
from problem_02 import rotate  # noqa: E402
# ---- End of generated header ----

import random


class TestRotateArray(TestCase):
    def test_example_1(self) -> None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_example_2_with_negatives(self) -> None:
        nums = [-1, -100, 3, 99]
        rotate(nums, 2)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_example_3_k_multiple_of_length(self) -> None:
        nums = [1, 2]
        rotate(nums, 4)
        self.assertEqual(nums, [1, 2])

    def test_single_element(self) -> None:
        nums = [42]
        rotate(nums, 1000)
        self.assertEqual(nums, [42])

    def test_zero_steps(self) -> None:
        nums = [1, 2, 3, 4]
        rotate(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_duplicates_and_zeros(self) -> None:
        nums = [0, 0, 1, 1, 0]
        rotate(nums, 2)
        self.assertEqual(nums, [1, 0, 0, 0, 1])

    def test_k_larger_than_length(self) -> None:
        nums = [1, 2, 3]
        rotate(nums, 7)  # 7 % 3 = 1
        self.assertEqual(nums, [3, 1, 2])

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        size = 100_000
        nums = [rng.randint(-1000, 1000) for _ in range(size)]
        k = 10**9 + 37
        effective_k = k % size
        expected = nums[-effective_k:] + nums[:-effective_k]

        rotate(nums, k)
        self.assertEqual(nums, expected)
