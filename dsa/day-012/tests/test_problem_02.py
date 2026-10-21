# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import StockSpanner  # noqa: E402
# ---- End of generated header ----

import random


class TestStockSpanner(TestCase):
    def test_example_one(self) -> None:
        spanner = StockSpanner()
        prices = [100, 80, 60, 70, 60, 75, 85]
        expected = [1, 1, 1, 2, 1, 4, 6]
        actual = [spanner.next(p) for p in prices]
        self.assertEqual(actual, expected)

    def test_strictly_increasing(self) -> None:
        spanner = StockSpanner()
        prices = [10, 20, 30, 40, 50]
        expected = [1, 2, 3, 4, 5]
        actual = [spanner.next(p) for p in prices]
        self.assertEqual(actual, expected)

    def test_strictly_decreasing(self) -> None:
        spanner = StockSpanner()
        prices = [50, 40, 30, 20, 10]
        expected = [1, 1, 1, 1, 1]
        actual = [spanner.next(p) for p in prices]
        self.assertEqual(actual, expected)

    def test_all_equal_prices(self) -> None:
        spanner = StockSpanner()
        prices = [42, 42, 42, 42, 42]
        expected = [1, 2, 3, 4, 5]
        actual = [spanner.next(p) for p in prices]
        self.assertEqual(actual, expected)

    def test_single_element(self) -> None:
        spanner = StockSpanner()
        self.assertEqual(spanner.next(100), 1)

    def test_v_shape_pattern(self) -> None:
        spanner = StockSpanner()
        prices = [100, 50, 25, 50, 100, 120]
        # At the second 50: 50, 25, and previous 50 are all <= 50, so span is 3.
        expected = [1, 1, 1, 3, 5, 6]
        actual = [spanner.next(p) for p in prices]
        self.assertEqual(actual, expected)

    def test_large_random_stream(self) -> None:
        # Ensure amortized O(1) performance on a large sequence
        rng = random.Random(42)
        prices = [rng.randint(1, 1000) for _ in range(10000)]

        # Compute reference spans using simple O(N^2) backward search on first 300 items
        sample_size = 300
        sample_prices = prices[:sample_size]
        sample_expected = []
        for i in range(sample_size):
            count = 0
            for j in range(i, -1, -1):
                if sample_prices[j] <= sample_prices[i]:
                    count += 1
                else:
                    break
            sample_expected.append(count)

        spanner = StockSpanner()
        actual_full = [spanner.next(p) for p in prices]
        self.assertEqual(actual_full[:sample_size], sample_expected)
        self.assertEqual(len(actual_full), 10000)
