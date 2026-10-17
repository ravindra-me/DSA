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
from problem_02 import ResettableCounters  # noqa: E402
# ---- End of generated header ----

import random


class TestResettableCounters(TestCase):
    def test_example_one(self) -> None:
        rc = ResettableCounters(3)
        rc.increment(0)
        rc.set_all(5)
        rc.increment(1)
        self.assertEqual([rc.get(0), rc.get(1), rc.get(2)], [5, 6, 5])

    def test_example_two_single_element_initial(self) -> None:
        rc = ResettableCounters(1)
        self.assertEqual(rc.get(0), 0)

    def test_single_element_modifications(self) -> None:
        rc = ResettableCounters(1)
        rc.increment(0)
        self.assertEqual(rc.get(0), 1)
        rc.increment(0)
        self.assertEqual(rc.get(0), 2)
        rc.set_all(100)
        self.assertEqual(rc.get(0), 100)
        rc.increment(0)
        self.assertEqual(rc.get(0), 101)

    def test_consecutive_set_all(self) -> None:
        rc = ResettableCounters(4)
        rc.increment(0)
        rc.increment(2)
        rc.set_all(10)
        rc.set_all(20)
        rc.set_all(0)
        for i in range(4):
            self.assertEqual(rc.get(i), 0)

    def test_boundary_indices_and_large_values(self) -> None:
        n = 5
        rc = ResettableCounters(n)
        large_val = 10**9
        rc.set_all(large_val)
        rc.increment(0)
        rc.increment(n - 1)
        self.assertEqual(rc.get(0), large_val + 1)
        self.assertEqual(rc.get(n - 1), large_val + 1)
        self.assertEqual(rc.get(1), large_val)
        self.assertEqual(rc.get(n - 2), large_val)

    def test_interleaved_operations_correctness(self) -> None:
        size = 10
        rc = ResettableCounters(size)
        # Step 1: increment evens
        for i in range(0, size, 2):
            rc.increment(i)
        # Step 2: set_all to 7
        rc.set_all(7)
        # Step 3: increment odds
        for i in range(1, size, 2):
            rc.increment(i)

        expected = [7 if i % 2 == 0 else 8 for i in range(size)]
        actual = [rc.get(i) for i in range(size)]
        self.assertEqual(actual, expected)

    def test_large_input_performance(self) -> None:
        # 100,000 counters, 100,000 operations
        # An O(n) set_all would perform O(n * num_resets) ~ 10^9 operations and time out.
        size = 100_000
        rc = ResettableCounters(size)
        rng = random.Random(42)

        # Track a deterministic small reference subset: indices 0, 10, 50, 999
        watched = [0, 10, 50, 999]
        ref = {idx: 0 for idx in watched}

        for op_idx in range(50_000):
            choice = op_idx % 5
            if choice == 0:
                val = (op_idx * 7) % 1000
                rc.set_all(val)
                for w in watched:
                    ref[w] = val
            else:
                target = rng.randrange(size)
                rc.increment(target)
                if target in ref:
                    ref[target] += 1

        for w in watched:
            self.assertEqual(rc.get(w), ref[w])
