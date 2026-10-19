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
from problem_04 import MinStack  # noqa: E402
# ---- End of generated header ----

import random

class TestMinStack(TestCase):
    def test_example_1(self) -> None:
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(ms.get_min(), -3)
        ms.pop()
        self.assertEqual(ms.top(), 0)
        self.assertEqual(ms.get_min(), -2)

    def test_example_2_single_element(self) -> None:
        ms = MinStack()
        ms.push(5)
        self.assertEqual(ms.get_min(), 5)
        self.assertEqual(ms.top(), 5)

    def test_duplicate_values_and_multiple_mins(self) -> None:
        ms = MinStack()
        ms.push(2)
        ms.push(2)
        ms.push(1)
        ms.push(1)
        self.assertEqual(ms.get_min(), 1)
        ms.pop()
        self.assertEqual(ms.get_min(), 1)
        self.assertEqual(ms.top(), 1)
        ms.pop()
        self.assertEqual(ms.get_min(), 2)
        self.assertEqual(ms.top(), 2)

    def test_strictly_increasing_and_decreasing(self) -> None:
        ms = MinStack()
        # Decreasing push
        for v in [10, 8, 6, 4, 2]:
            ms.push(v)
            self.assertEqual(ms.get_min(), v)
            self.assertEqual(ms.top(), v)

        # Unwinding decreasing stack
        expected_mins = [2, 4, 6, 8, 10]
        for expected in expected_mins:
            self.assertEqual(ms.get_min(), expected)
            ms.pop()

    def test_extremes_and_negative_numbers(self) -> None:
        ms = MinStack()
        min_val = - (1 << 31)
        max_val = (1 << 31) - 1
        ms.push(0)
        ms.push(max_val)
        self.assertEqual(ms.get_min(), 0)
        self.assertEqual(ms.top(), max_val)
        ms.push(min_val)
        self.assertEqual(ms.get_min(), min_val)
        self.assertEqual(ms.top(), min_val)
        ms.pop()
        self.assertEqual(ms.get_min(), 0)
        self.assertEqual(ms.top(), max_val)

    def test_large_random_operations(self) -> None:
        ms = MinStack()
        ref_stack: list[int] = []
        rng = random.Random(42)

        for _ in range(10_000):
            # Push if empty or randomly choose push
            if not ref_stack or rng.random() < 0.65:
                val = rng.randint(-1_000_000, 1_000_000)
                ms.push(val)
                ref_stack.append(val)
            else:
                ms.pop()
                ref_stack.pop()

            self.assertEqual(ms.top(), ref_stack[-1])
            self.assertEqual(ms.get_min(), min(ref_stack))
