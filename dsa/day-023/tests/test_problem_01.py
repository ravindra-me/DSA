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
from problem_01 import subsets_bitmask  # noqa: E402
# ---- End of generated header ----

class TestSubsetsBitmask(TestCase):
    def test_example_one(self):
        nums = [1, 2, 3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(subsets_bitmask(nums), expected)

    def test_example_two(self):
        nums = [0]
        expected = [[], [0]]
        self.assertEqual(subsets_bitmask(nums), expected)

    def test_negative_numbers(self):
        nums = [-5, -2]
        expected = [[], [-5], [-2], [-5, -2]]
        self.assertEqual(subsets_bitmask(nums), expected)

    def test_size_ordering(self):
        nums = [10, 20, 30, 40]
        res = subsets_bitmask(nums)
        self.assertEqual(len(res), 16)
        sizes = [len(subset) for subset in res]
        self.assertEqual(sizes, sorted(sizes))

    def test_two_elements(self):
        nums = [7, 8]
        expected = [[], [7], [8], [7, 8]]
        self.assertEqual(subsets_bitmask(nums), expected)

    def test_max_constraint_count_and_types(self):
        nums = list(range(1, 16))
        res = subsets_bitmask(nums)
        self.assertEqual(len(res), 1 << 15)
        self.assertEqual(res[0], [])
        self.assertEqual(res[-1], nums)
        singletons = [s for s in res if len(s) == 1]
        self.assertEqual(len(singletons), 15)
        self.assertEqual([s[0] for s in singletons], nums)
