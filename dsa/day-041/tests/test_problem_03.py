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
from problem_03 import TwoStackDeque  # noqa: E402
# ---- End of generated header ----

import collections
import random

class TestTwoStackDeque(TestCase):
    def test_example_1(self) -> None:
        d = TwoStackDeque()
        d.push_back(1)
        d.push_back(2)
        d.push_front(0)
        self.assertEqual(d.peek_front(), 0)
        self.assertEqual(d.pop_back(), 2)
        self.assertEqual(d.pop_front(), 0)
        self.assertEqual(len(d), 1)
        self.assertEqual(d.pop_front(), 1)
        self.assertIsNone(d.pop_front())

    def test_empty_operations(self) -> None:
        d = TwoStackDeque()
        self.assertEqual(len(d), 0)
        self.assertIsNone(d.pop_front())
        self.assertIsNone(d.pop_back())
        self.assertIsNone(d.peek_front())
        self.assertIsNone(d.peek_back())

    def test_single_element_front_and_back(self) -> None:
        d = TwoStackDeque()
        d.push_front(42)
        self.assertEqual(len(d), 1)
        self.assertEqual(d.peek_back(), 42)
        self.assertEqual(d.peek_front(), 42)
        self.assertEqual(d.pop_back(), 42)
        self.assertEqual(len(d), 0)

        d.push_back(99)
        self.assertEqual(d.peek_front(), 99)
        self.assertEqual(d.peek_back(), 99)
        self.assertEqual(d.pop_front(), 99)
        self.assertEqual(len(d), 0)

    def test_negative_values_and_duplicates(self) -> None:
        d = TwoStackDeque()
        values = [-10, 0, 5, -10, 0]
        for v in values:
            d.push_back(v)
        self.assertEqual(len(d), 5)
        for v in values:
            self.assertEqual(d.pop_front(), v)
        self.assertIsNone(d.pop_front())

    def test_alternating_pops(self) -> None:
        d = TwoStackDeque()
        for i in range(10):
            d.push_back(i)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(d.pop_front(), 0)
        self.assertEqual(d.pop_back(), 9)
        self.assertEqual(d.pop_front(), 1)
        self.assertEqual(d.pop_back(), 8)
        self.assertEqual(len(d), 6)

    def test_large_random_operations(self) -> None:
        rng = random.Random(1337)
        d = TwoStackDeque()
        ref = collections.deque()

        for _ in range(20000):
            op = rng.randint(0, 5)
            val = rng.randint(-1000, 1000)
            if op == 0:
                d.push_front(val)
                ref.appendleft(val)
            elif op == 1:
                d.push_back(val)
                ref.append(val)
            elif op == 2:
                expected = ref.popleft() if ref else None
                self.assertEqual(d.pop_front(), expected)
            elif op == 3:
                expected = ref.pop() if ref else None
                self.assertEqual(d.pop_back(), expected)
            elif op == 4:
                expected = ref[0] if ref else None
                self.assertEqual(d.peek_front(), expected)
            elif op == 5:
                expected = ref[-1] if ref else None
                self.assertEqual(d.peek_back(), expected)
            self.assertEqual(len(d), len(ref))
