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
from problem_01 import contains_duplicate  # noqa: E402
# ---- End of generated header ----

class TestContainsDuplicate(TestCase):
    def test_example_1(self) -> None:
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))

    def test_example_2(self) -> None:
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_example_3_single_element(self) -> None:
        self.assertFalse(contains_duplicate([42]))

    def test_all_identical_elements(self) -> None:
        self.assertTrue(contains_duplicate([7, 7, 7, 7]))

    def test_negative_numbers_and_zero(self) -> None:
        self.assertFalse(contains_duplicate([-1, 0, 1, -2, 2]))
        self.assertTrue(contains_duplicate([-5, 10, -5, 0]))

    def test_duplicate_at_boundaries(self) -> None:
        # Duplicate is at the first and last positions
        self.assertTrue(contains_duplicate([99, 1, 2, 3, 4, 99]))

    def test_large_input_distinct(self) -> None:
        # 100_000 distinct values: naive O(n^2) would time out, O(n) runs in < 0.1s
        large_distinct = list(range(100_000))
        self.assertFalse(contains_duplicate(large_distinct))

    def test_large_input_duplicate_at_end(self) -> None:
        large_with_dup = list(range(100_000))
        large_with_dup.append(0)  # duplicate of the first element at the end
        self.assertTrue(contains_duplicate(large_with_dup))
