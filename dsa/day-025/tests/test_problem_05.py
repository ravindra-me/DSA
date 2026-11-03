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
from problem_05 import StreamPeakFinder  # noqa: E402
# ---- End of generated header ----

import unittest
import random

class TestStreamPeakFinder(unittest.TestCase):
    def test_example_1(self):
        finder = StreamPeakFinder()
        self.assertIsNone(finder.process(3))
        self.assertIsNone(finder.process(7))
        self.assertEqual(finder.process(2), 7)

    def test_example_2(self):
        finder = StreamPeakFinder()
        self.assertIsNone(finder.process(1))
        self.assertIsNone(finder.process(2))
        self.assertIsNone(finder.process(3))

    def test_short_stream(self):
        finder = StreamPeakFinder()
        self.assertIsNone(finder.process(10))
        self.assertIsNone(finder.process(5))

    def test_duplicates(self):
        finder = StreamPeakFinder()
        # Plateau 5, 5, 5 should not yield peaks
        self.assertIsNone(finder.process(5))
        self.assertIsNone(finder.process(5))
        self.assertIsNone(finder.process(5))
        # Strict peak check: 5 < 7 > 7 -> False
        self.assertIsNone(finder.process(7))
        self.assertIsNone(finder.process(7))

    def test_negative_numbers(self):
        finder = StreamPeakFinder()
        self.assertIsNone(finder.process(-10))
        self.assertIsNone(finder.process(-3))
        self.assertEqual(finder.process(-5), -3)

    def test_multiple_peaks(self):
        finder = StreamPeakFinder()
        stream = [1, 4, 2, 8, 3, 10, 5]
        expected = [None, None, 4, None, 8, None, 10]
        results = [finder.process(x) for x in stream]
        self.assertEqual(results, expected)

    def test_large_stream(self):
        rng = random.Random(42)
        values = [rng.randint(-10**9, 10**9) for _ in range(50000)]
        finder = StreamPeakFinder()
        
        results = [finder.process(v) for v in values]
        
        # Verify against reference computation
        expected = [None] * len(values)
        for i in range(2, len(values)):
            if values[i - 2] < values[i - 1] and values[i - 1] > values[i]:
                expected[i] = values[i - 1]
                
        self.assertEqual(results, expected)
