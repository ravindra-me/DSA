# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import RecentCounter  # noqa: E402
# ---- End of generated header ----

import random
from collections import deque


class TestRecentCounter(TestCase):
    def test_example_one(self) -> None:
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(100), 2)
        self.assertEqual(rc.ping(3001), 3)
        self.assertEqual(rc.ping(3002), 3)

    def test_example_two(self) -> None:
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(4000), 1)

    def test_single_call(self) -> None:
        rc = RecentCounter()
        self.assertEqual(rc.ping(10), 1)

    def test_exact_boundary_retention(self) -> None:
        rc = RecentCounter()
        self.assertEqual(rc.ping(1000), 1)
        # 4000 - 3000 = 1000, boundary is inclusive so 1000 should remain
        self.assertEqual(rc.ping(4000), 2)
        # 4001 - 3000 = 1001, 1000 should now be excluded
        self.assertEqual(rc.ping(4001), 2)

    def test_large_time_jumps(self) -> None:
        rc = RecentCounter()
        timestamps = [1, 10000, 100000, 1000000, 1000000000]
        for t in timestamps:
            self.assertEqual(rc.ping(t), 1)

    def test_consecutive_dense_calls(self) -> None:
        rc = RecentCounter()
        # 3000 calls 1 millisecond apart
        for t in range(1, 3001):
            self.assertEqual(rc.ping(t), t)
        # The 3001st call should still contain all 3001 calls: [1, 3001]
        self.assertEqual(rc.ping(3001), 3001)
        # At 3002, t=1 falls out, total should stay 3001
        self.assertEqual(rc.ping(3002), 3001)

    def test_large_deterministic_workload(self) -> None:
        rc = RecentCounter()
        rng = random.Random(42)
        current_time = 0
        history: deque[int] = deque()

        for _ in range(10000):
            # Strictly increasing timestamps
            current_time += rng.randint(1, 20)
            history.append(current_time)
            min_allowed = current_time - 3000
            while history and history[0] < min_allowed:
                history.popleft()
            expected = len(history)
            self.assertEqual(rc.ping(current_time), expected)
