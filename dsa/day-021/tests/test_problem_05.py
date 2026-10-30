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
from problem_05 import corp_flight_bookings  # noqa: E402
# ---- End of generated header ----

class TestCorpFlightBookings(TestCase):
    def test_example_1(self) -> None:
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        n = 5
        expected = [10, 55, 45, 25, 25]
        self.assertEqual(corp_flight_bookings(bookings, n), expected)

    def test_example_2(self) -> None:
        bookings = [[1, 2, 10], [2, 2, 15]]
        n = 2
        expected = [10, 25]
        self.assertEqual(corp_flight_bookings(bookings, n), expected)

    def test_single_flight(self) -> None:
        bookings = [[1, 1, 5], [1, 1, 10]]
        n = 1
        self.assertEqual(corp_flight_bookings(bookings, n), [15])

    def test_full_range_single_booking(self) -> None:
        bookings = [[1, 4, 100]]
        n = 4
        self.assertEqual(corp_flight_bookings(bookings, n), [100, 100, 100, 100])

    def test_non_overlapping_bookings(self) -> None:
        bookings = [[1, 1, 10], [3, 3, 30], [5, 5, 50]]
        n = 5
        self.assertEqual(corp_flight_bookings(bookings, n), [10, 0, 30, 0, 50])

    def test_disjoint_and_overlapping_mixed(self) -> None:
        bookings = [[1, 3, 10], [2, 4, 20], [4, 5, 30]]
        n = 5
        # Flight 1: 10
        # Flight 2: 10 + 20 = 30
        # Flight 3: 10 + 20 = 30
        # Flight 4: 20 + 30 = 50
        # Flight 5: 30
        self.assertEqual(corp_flight_bookings(bookings, n), [10, 30, 30, 50, 30])

    def test_large_input_performance(self) -> None:
        import random
        rng = random.Random(42)
        n = 10_000
        m = 10_000
        bookings = []
        
        # Deterministic generation with known contribution
        # Add a baseline booking spanning the whole flight range
        bookings.append([1, n, 5])
        
        # Generate arbitrary intervals
        for _ in range(m - 1):
            f = rng.randint(1, n)
            l = rng.randint(f, n)
            s = rng.randint(1, 100)
            bookings.append([f, l, s])

        # Compute expected using reference sweep-line / difference array verification
        expected_diff = [0] * (n + 1)
        for f, l, s in bookings:
            expected_diff[f - 1] += s
            expected_diff[l] -= s
        
        expected = []
        cur = 0
        for i in range(n):
            cur += expected_diff[i]
            expected.append(cur)

        actual = corp_flight_bookings(bookings, n)
        self.assertEqual(actual, expected)
