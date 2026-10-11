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
from problem_01 import remove_element  # noqa: E402
# ---- End of generated header ----

class TestRemoveElement(TestCase):
    def test_example_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = remove_element(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_example_2_empty(self):
        nums = []
        val = 0
        k = remove_element(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_example_3(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = remove_element(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_all_elements_match(self):
        nums = [7, 7, 7, 7]
        val = 7
        k = remove_element(nums, val)
        self.assertEqual(k, 0)

    def test_no_elements_match(self):
        nums = [1, 2, 3, 4]
        val = 5
        k = remove_element(nums, val)
        self.assertEqual(k, 4)
        self.assertEqual(sorted(nums[:k]), [1, 2, 3, 4])

    def test_single_element_cases(self):
        nums_matching = [42]
        self.assertEqual(remove_element(nums_matching, 42), 0)

        nums_non_matching = [42]
        self.assertEqual(remove_element(nums_non_matching, 10), 1)
        self.assertEqual(nums_non_matching[:1], [42])

    def test_large_array_performance(self):
        import random
        rng = random.Random(42)
        n = 100_000
        val = 50
        nums = [rng.randint(0, 100) for _ in range(n)]
        expected_remaining = [x for x in nums if x != val]
        expected_k = len(expected_remaining)

        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], expected_remaining)
