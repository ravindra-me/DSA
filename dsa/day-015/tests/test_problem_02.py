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
from problem_02 import RecentCounter  # noqa: E402
# ---- End of generated header ----

import random
from collections import deque


class TestRecentCounter(TestCase):
    def test_example_1(self) -> None:
        counter = RecentCounter()
        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(100), 2)
        self.assertEqual(counter.ping(3001), 3)
        self.assertEqual(counter.ping(3002), 3)

    def test_example_2_large_gap(self) -> None:
        counter = RecentCounter()
        self.assertEqual(counter.ping(10), 1)
        self.assertEqual(counter.ping(4000), 1)

    def test_exact_boundary_retention(self) -> None:
        counter = RecentCounter()
        self.assertEqual(counter.ping(1000), 1)
        # 4000 - 3000 = 1000, exactly inclusive boundary
        self.assertEqual(counter.ping(4000), 2)
        # 4001 - 3000 = 1001, 1000 is now evicted
        self.assertEqual(counter.ping(4001), 2)

    def test_single_call(self) -> None:
        counter = RecentCounter()
        self.assertEqual(counter.ping(1), 1)

    def test_dense_burst_calls(self) -> None:
        counter = RecentCounter()
        for i in range(1, 101):
            self.assertEqual(counter.ping(i), i)

    def test_large_number_of_calls(self) -> None:
        counter = RecentCounter()
        rng = random.Random(42)
        current_t = 0
        history: deque[int] = deque()

        for _ in range(20000):
            current_t += rng.randint(1, 5)
            history.append(current_t)
            while history and history[0] < current_t - 3000:
                history.popleft()
            expected = len(history)
            self.assertEqual(counter.ping(current_t), expected)
