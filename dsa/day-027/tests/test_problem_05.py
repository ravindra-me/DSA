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
from problem_05 import search_rotated  # noqa: E402
# ---- End of generated header ----

class TestSearchRotated(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_example_2(self):
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_example_3(self):
        self.assertEqual(search_rotated([1], 0), -1)

    def test_single_element_found(self):
        self.assertEqual(search_rotated([5], 5), 0)

    def test_no_rotation(self):
        self.assertEqual(search_rotated([1, 2, 3, 4, 5], 4), 3)

    def test_two_elements(self):
        self.assertEqual(search_rotated([3, 1], 1), 1)
        self.assertEqual(search_rotated([3, 1], 3), 0)
        self.assertEqual(search_rotated([3, 1], 2), -1)

    def test_large_input(self):
        # Create a large sorted list and rotate it
        size = 5000
        pivot = 1234
        arr = list(range(size))
        rotated = arr[pivot:] + arr[:pivot]
        # Target is at index (size - pivot) + 500 = 4266
        target = 500
        self.assertEqual(search_rotated(rotated, target), 4266)
        self.assertEqual(search_rotated(rotated, -1), -1)
