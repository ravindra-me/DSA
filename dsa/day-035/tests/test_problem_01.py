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
from problem_01 import count_visible_mountains  # noqa: E402
# ---- End of generated header ----

import random
from unittest import TestCase

class TestVisibleMountainsCount(TestCase):
    def test_example_1(self):
        heights = [10, 6, 8, 5, 11]
        expected = [3, 1, 2, 1, 0]
        self.assertEqual(count_visible_mountains(heights), expected)

    def test_example_2(self):
        heights = [5, 4, 3, 2, 1]
        expected = [1, 1, 1, 1, 0]
        self.assertEqual(count_visible_mountains(heights), expected)

    def test_single_element(self):
        self.assertEqual(count_visible_mountains([42]), [0])

    def test_empty(self):
        self.assertEqual(count_visible_mountains([]), [])

    def test_increasing(self):
        heights = [1, 2, 3, 4, 5]
        expected = [1, 1, 1, 1, 0]
        self.assertEqual(count_visible_mountains(heights), expected)

    def test_equal_heights(self):
        heights = [5, 5, 5, 5]
        expected = [1, 1, 1, 0]
        self.assertEqual(count_visible_mountains(heights), expected)

    def test_v_shape(self):
        heights = [10, 2, 1, 3, 12]
        # 10 sees 2, 3, 12 -> 3
        # 2 sees 1, 3 -> 2
        # 1 sees 3 -> 1
        # 3 sees 12 -> 1
        # 12 sees 0 -> 0
        expected = [3, 2, 1, 1, 0]
        self.assertEqual(count_visible_mountains(heights), expected)

    def test_large_performance(self):
        rng = random.Random(42)
        n = 100000
        heights = [rng.randint(1, 10**9) for _ in range(n)]
        result = count_visible_mountains(heights)
        self.assertEqual(len(result), n)
        self.assertEqual(result[-1], 0)
