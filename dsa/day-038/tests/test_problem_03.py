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
from problem_03 import OverwriteBuffer  # noqa: E402
# ---- End of generated header ----

import random


class TestOverwriteBuffer(TestCase):
    def test_example_1(self) -> None:
        buf = OverwriteBuffer(3)
        buf.push(1)
        buf.push(2)
        buf.push(3)
        buf.push(4)  # Overwrites 1
        self.assertEqual(buf.get_last_k(2), [3, 4])
        self.assertEqual(buf.pop_oldest(), 2)
        self.assertEqual(buf.get_last_k(2), [3, 4])

    def test_empty_buffer(self) -> None:
        buf = OverwriteBuffer(2)
        self.assertEqual(buf.pop_oldest(), -1)
        self.assertEqual(buf.get_last_k(1), [])
        self.assertEqual(buf.get_last_k(2), [])

    def test_capacity_one(self) -> None:
        buf = OverwriteBuffer(1)
        buf.push(42)
        self.assertEqual(buf.get_last_k(1), [42])
        buf.push(99)
        self.assertEqual(buf.get_last_k(1), [99])
        self.assertEqual(buf.pop_oldest(), 99)
        self.assertEqual(buf.pop_oldest(), -1)
        self.assertEqual(buf.get_last_k(1), [])

    def test_request_more_than_size(self) -> None:
        buf = OverwriteBuffer(5)
        buf.push(10)
        buf.push(20)
        self.assertEqual(buf.get_last_k(5), [10, 20])
        self.assertEqual(buf.get_last_k(2), [10, 20])
        self.assertEqual(buf.get_last_k(1), [20])

    def test_wraparound_and_pop_sequence(self) -> None:
        buf = OverwriteBuffer(3)
        for i in range(10):
            buf.push(i)
        # Last 3 pushed are 7, 8, 9
        self.assertEqual(buf.get_last_k(3), [7, 8, 9])
        self.assertEqual(buf.pop_oldest(), 7)
        self.assertEqual(buf.get_last_k(3), [8, 9])
        buf.push(100)
        self.assertEqual(buf.get_last_k(3), [8, 9, 100])
        self.assertEqual(buf.pop_oldest(), 8)
        self.assertEqual(buf.pop_oldest(), 9)
        self.assertEqual(buf.pop_oldest(), 100)
        self.assertEqual(buf.pop_oldest(), -1)

    def test_zero_and_duplicate_values(self) -> None:
        buf = OverwriteBuffer(4)
        buf.push(0)
        buf.push(0)
        buf.push(10)
        buf.push(0)
        self.assertEqual(buf.get_last_k(4), [0, 0, 10, 0])
        self.assertEqual(buf.pop_oldest(), 0)
        self.assertEqual(buf.pop_oldest(), 0)
        self.assertEqual(buf.pop_oldest(), 10)
        self.assertEqual(buf.pop_oldest(), 0)
        self.assertEqual(buf.pop_oldest(), -1)

    def test_stress_and_consistency(self) -> None:
        rng = random.Random(1337)
        capacity = 200
        buf = OverwriteBuffer(capacity)
        reference: list[int] = []

        for _ in range(5000):
            op = rng.choice(["push", "push", "push", "pop", "get"])
            if op == "push":
                val = rng.randint(0, 10**6)
                buf.push(val)
                if len(reference) == capacity:
                    reference.pop(0)
                reference.append(val)
            elif op == "pop":
                expected = reference.pop(0) if reference else -1
                self.assertEqual(buf.pop_oldest(), expected)
            else:
                m = rng.randint(1, capacity)
                expected = reference[-m:] if reference else []
                self.assertEqual(buf.get_last_k(m), expected)
