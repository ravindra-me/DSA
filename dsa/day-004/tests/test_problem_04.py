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
from problem_04 import nested_sum  # noqa: E402
# ---- End of generated header ----

class TestNestedSum(TestCase):
    def test_example_case(self):
        self.assertEqual(nested_sum([1, [2, 3], [[4]]]), 10)

    def test_empty_list(self):
        self.assertEqual(nested_sum([]), 0)
        self.assertEqual(nested_sum([[], [[]]]), 0)

    def test_single_element(self):
        self.assertEqual(nested_sum([5]), 5)
        self.assertEqual(nested_sum([[5]]), 5)

    def test_negative_numbers(self):
        self.assertEqual(nested_sum([-1, [2, -3], [[4]]]), 2)

    def test_mixed_structure(self):
        self.assertEqual(nested_sum([10, [10, [10, [10]]], 10]), 50)

    def test_large_input_performance(self):
        # Construct a deeply nested list: [[[[... 1000 times ...]]]]
        # This tests recursion depth management.
        deep_list = [1]
        for _ in range(1000):
            deep_list = [deep_list]
        self.assertEqual(nested_sum(deep_list), 1)

    def test_many_elements(self):
        # Large number of elements: [1, 1, 1, ..., 1]
        large_input = [1] * 10000
        self.assertEqual(nested_sum(large_input), 10000)
