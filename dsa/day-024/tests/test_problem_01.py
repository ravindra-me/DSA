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
from problem_01 import find_max_average  # noqa: E402
# ---- End of generated header ----

import random


class TestFindMaxAverage(TestCase):
    def test_example_one(self) -> None:
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        self.assertAlmostEqual(find_max_average(nums, k), 12.75, places=5)

    def test_example_two(self) -> None:
        nums = [5]
        k = 1
        self.assertAlmostEqual(find_max_average(nums, k), 5.0, places=5)

    def test_k_equals_length(self) -> None:
        nums = [1, 2, 3, 4, 5]
        k = 5
        self.assertAlmostEqual(find_max_average(nums, k), 3.0, places=5)

    def test_all_negative_numbers(self) -> None:
        nums = [-5, -2, -8, -1, -4]
        k = 2
        # Windows of size 2: [-5, -2] -> -3.5, [-2, -8] -> -5.0, [-8, -1] -> -4.5, [-1, -4] -> -2.5
        self.assertAlmostEqual(find_max_average(nums, k), -2.5, places=5)

    def test_all_identical_elements(self) -> None:
        nums = [7, 7, 7, 7, 7]
        k = 3
        self.assertAlmostEqual(find_max_average(nums, k), 7.0, places=5)

    def test_k_is_one_with_negatives_and_zeros(self) -> None:
        nums = [-10, 0, -2, -5]
        k = 1
        self.assertAlmostEqual(find_max_average(nums, k), 0.0, places=5)

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        n = 100_000
        k = 25_000
        nums = [rng.randint(-1000, 1000) for _ in range(n)]
        # Plant an artificially high contiguous segment to ensure correctness
        target_start = 50_000
        for i in range(target_start, target_start + k):
            nums[i] = 10_000

        result = find_max_average(nums, k)
        self.assertAlmostEqual(result, 10_000.0, places=5)
