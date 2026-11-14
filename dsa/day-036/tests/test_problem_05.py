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
from problem_05 import partial_heap_sort  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestPartialHeapSort(TestCase):
    def _verify_partial_sort(self, original: list[int], modified: list[int], k: int) -> None:
        # Check multiset conservation
        self.assertEqual(Counter(original), Counter(modified))
        n = len(original)
        k = min(k, n)
        if k == 0:
            return
        # Check that last k elements are sorted
        last_k = modified[n - k:]
        self.assertEqual(last_k, sorted(last_k))
        # Check that each element in last k is >= each element in first n-k
        if n > k:
            max_prefix = max(modified[:n - k])
            min_suffix = min(last_k)
            self.assertLessEqual(max_prefix, min_suffix)

    def test_example_1(self) -> None:
        nums = [9, 3, 7, 1, 8, 2, 5]
        orig = list(nums)
        k = 3
        partial_heap_sort(nums, k)
        self.assertEqual(nums[len(nums) - k:], [7, 8, 9])
        self._verify_partial_sort(orig, nums, k)

    def test_example_2_k_zero(self) -> None:
        nums = [4, 1, 2]
        orig = list(nums)
        partial_heap_sort(nums, 0)
        self._verify_partial_sort(orig, nums, 0)

    def test_empty_and_single_element(self) -> None:
        empty: list[int] = []
        partial_heap_sort(empty, 0)
        self.assertEqual(empty, [])

        single = [42]
        partial_heap_sort(single, 1)
        self.assertEqual(single, [42])

    def test_k_equals_len(self) -> None:
        nums = [5, 2, 8, 1, 9, 3]
        orig = list(nums)
        partial_heap_sort(nums, len(nums))
        self.assertEqual(nums, sorted(orig))

    def test_duplicate_values(self) -> None:
        nums = [4, 2, 4, 3, 2, 4, 1]
        orig = list(nums)
        k = 4
        partial_heap_sort(nums, k)
        self._verify_partial_sort(orig, nums, k)

    def test_negative_numbers_and_zero(self) -> None:
        nums = [-10, 0, -50, 15, -1, 4, 0]
        orig = list(nums)
        k = 3
        partial_heap_sort(nums, k)
        self._verify_partial_sort(orig, nums, k)

    def test_large_random_input(self) -> None:
        rng = random.Random(42)
        n = 10_000
        k = 150
        nums = [rng.randint(-100_000, 100_000) for _ in range(n)]
        orig = list(nums)
        partial_heap_sort(nums, k)
        self._verify_partial_sort(orig, nums, k)
