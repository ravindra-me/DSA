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
from problem_01 import sort_array_by_parity_ii  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestSortArrayByParityII(TestCase):
    def _validate_parity(self, original: list[int], result: list[int]) -> None:
        # Verify result is the same object mutated in-place
        self.assertIs(result, original)
        # Verify multiset of elements is preserved
        self.assertEqual(Counter(original), Counter(result))
        # Verify parity condition
        for i, val in enumerate(result):
            if i % 2 == 0:
                self.assertEqual(val % 2, 0, f"Expected even at index {i}, got {val}")
            else:
                self.assertEqual(val % 2, 1, f"Expected odd at index {i}, got {val}")

    def test_example_1(self) -> None:
        nums = [4, 2, 5, 7]
        result = sort_array_by_parity_ii(nums)
        self._validate_parity(nums, result)

    def test_example_2(self) -> None:
        nums = [2, 3]
        result = sort_array_by_parity_ii(nums)
        self._validate_parity(nums, result)

    def test_already_sorted_larger(self) -> None:
        nums = [0, 1, 2, 3, 4, 5, 6, 7]
        result = sort_array_by_parity_ii(nums)
        self._validate_parity(nums, result)

    def test_completely_reversed_parity(self) -> None:
        nums = [1, 0, 3, 2, 5, 4, 7, 6]
        result = sort_array_by_parity_ii(nums)
        self._validate_parity(nums, result)

    def test_with_duplicates_and_zeros(self) -> None:
        nums = [0, 0, 0, 1, 1, 1]
        result = sort_array_by_parity_ii(nums)
        self._validate_parity(nums, result)

    def test_minimum_size_inverted(self) -> None:
        nums = [3, 2]
        result = sort_array_by_parity_ii(nums)
        self._validate_parity(nums, result)
        self.assertEqual(result, [2, 3])

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        n = 20_000
        evens = [rng.randrange(0, 1001, 2) for _ in range(n // 2)]
        odds = [rng.randrange(1, 1001, 2) for _ in range(n // 2)]
        nums = evens + odds
        rng.shuffle(nums)

        initial_counts = Counter(nums)
        result = sort_array_by_parity_ii(nums)
        self.assertIs(result, nums)
        self.assertEqual(Counter(result), initial_counts)
        for i, val in enumerate(result):
            self.assertEqual(val % 2, i % 2)
