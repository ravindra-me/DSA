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
from problem_04 import sort_k_messed_array  # noqa: E402
# ---- End of generated header ----

import random


class TestSortKMessedArray(TestCase):
    def test_example_1(self):
        nums = [3, 2, 1, 5, 4, 7, 6, 5]
        k = 3
        expected = sorted(nums)
        self.assertEqual(sort_k_messed_array(nums, k), expected)

    def test_example_2_k_zero(self):
        nums = [1, 2, 3]
        k = 0
        self.assertEqual(sort_k_messed_array(nums, k), [1, 2, 3])

    def test_empty_and_single_element(self):
        self.assertEqual(sort_k_messed_array([], 0), [])
        self.assertEqual(sort_k_messed_array([42], 0), [42])

    def test_negative_and_duplicates(self):
        nums = [-3, -5, -4, 0, -1, 2, 1]
        k = 2
        expected = sorted(nums)
        self.assertEqual(sort_k_messed_array(nums, k), expected)

    def test_all_elements_identical(self):
        nums = [7, 7, 7, 7, 7]
        k = 2
        self.assertEqual(sort_k_messed_array(nums, k), [7, 7, 7, 7, 7])

    def test_k_equals_len_minus_one(self):
        nums = [5, 4, 3, 2, 1]
        k = 4
        self.assertEqual(sort_k_messed_array(nums, k), [1, 2, 3, 4, 5])

    def test_large_input_k_bounded(self):
        rng = random.Random(1337)
        n = 20_000
        k = 15
        sorted_nums = sorted(rng.randint(-10**9, 10**9) for _ in range(n))
        nums = list(sorted_nums)
        
        # Permute within disjoint blocks of size (k + 1) to strictly guarantee
        # that no element moves more than k indices from its sorted location.
        block_size = k + 1
        for start in range(0, n, block_size):
            end = min(n, start + block_size)
            block = nums[start:end]
            rng.shuffle(block)
            nums[start:end] = block

        result = sort_k_messed_array(nums, k)
        self.assertEqual(result, sorted_nums)
