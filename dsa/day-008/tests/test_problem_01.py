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
from problem_01 import num_subarray_product_less_than_k  # noqa: E402
# ---- End of generated header ----

class TestSubarrayProductLessThanK(TestCase):
    def test_example_1(self):
        self.assertEqual(num_subarray_product_less_than_k([10, 5, 2, 6], 100), 8)

    def test_example_2_zero_k(self):
        self.assertEqual(num_subarray_product_less_than_k([1, 2, 3], 0), 0)

    def test_k_is_one(self):
        self.assertEqual(num_subarray_product_less_than_k([1, 2, 3], 1), 0)

    def test_single_element(self):
        self.assertEqual(num_subarray_product_less_than_k([5], 6), 1)
        self.assertEqual(num_subarray_product_less_than_k([5], 5), 0)
        self.assertEqual(num_subarray_product_less_than_k([5], 4), 0)

    def test_all_elements_valid(self):
        nums = [1, 1, 1, 1]
        k = 2
        expected = 4 * 5 // 2
        self.assertEqual(num_subarray_product_less_than_k(nums, k), expected)

    def test_no_elements_valid(self):
        nums = [10, 20, 30]
        k = 5
        self.assertEqual(num_subarray_product_less_than_k(nums, k), 0)

    def test_duplicate_values(self):
        nums = [2, 2, 2, 2]
        k = 8
        self.assertEqual(num_subarray_product_less_than_k(nums, k), 7)

    def test_large_input_linear_time(self):
        n = 30000
        nums = [1] * n
        k = 5
        expected = n * (n + 1) // 2
        self.assertEqual(num_subarray_product_less_than_k(nums, k), expected)
