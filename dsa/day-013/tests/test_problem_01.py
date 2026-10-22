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
from problem_01 import CircularQueue  # noqa: E402
# ---- End of generated header ----

import random


class TestCircularQueue(TestCase):
    def test_example_1(self) -> None:
        q = CircularQueue(3)
        self.assertTrue(q.enqueue(1))
        self.assertTrue(q.enqueue(2))
        self.assertTrue(q.enqueue(3))
        self.assertFalse(q.enqueue(4))
        self.assertEqual(q.rear(), 3)
        self.assertTrue(q.is_full())
        self.assertTrue(q.dequeue())
        self.assertTrue(q.enqueue(4))
        self.assertEqual(q.rear(), 4)

    def test_example_2_empty_state(self) -> None:
        q = CircularQueue(1)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.front(), -1)
        self.assertEqual(q.rear(), -1)
        self.assertFalse(q.dequeue())

    def test_capacity_one_lifecycle(self) -> None:
        q = CircularQueue(1)
        self.assertTrue(q.enqueue(42))
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.front(), 42)
        self.assertEqual(q.rear(), 42)
        self.assertFalse(q.enqueue(99))
        self.assertTrue(q.dequeue())
        self.assertTrue(q.is_empty())
        self.assertEqual(q.front(), -1)
        self.assertEqual(q.rear(), -1)

    def test_zero_and_duplicate_values(self) -> None:
        q = CircularQueue(4)
        self.assertTrue(q.enqueue(0))
        self.assertTrue(q.enqueue(0))
        self.assertTrue(q.enqueue(5))
        self.assertTrue(q.enqueue(5))
        self.assertEqual(q.front(), 0)
        self.assertEqual(q.rear(), 5)
        self.assertTrue(q.dequeue())
        self.assertEqual(q.front(), 0)
        self.assertTrue(q.dequeue())
        self.assertEqual(q.front(), 5)

    def test_multiple_wrap_arounds(self) -> None:
        k = 5
        q = CircularQueue(k)
        for cycle in range(10):
            base = cycle * 10
            for i in range(k):
                self.assertTrue(q.enqueue(base + i))
            self.assertTrue(q.is_full())
            self.assertEqual(q.front(), base)
            self.assertEqual(q.rear(), base + k - 1)
            for i in range(k):
                self.assertEqual(q.front(), base + i)
                self.assertTrue(q.dequeue())
            self.assertTrue(q.is_empty())

    def test_large_number_of_operations(self) -> None:
        rng = random.Random(42)
        k = 100
        q = CircularQueue(k)
        mirror: list[int] = []

        for _ in range(3000):
            op = rng.choice(["enqueue", "dequeue", "front", "rear", "is_empty", "is_full"])
            if op == "enqueue":
                val = rng.randint(0, 1000)
                if len(mirror) < k:
                    mirror.append(val)
                    self.assertTrue(q.enqueue(val))
                else:
                    self.assertFalse(q.enqueue(val))
            elif op == "dequeue":
                if mirror:
                    mirror.pop(0)
                    self.assertTrue(q.dequeue())
                else:
                    self.assertFalse(q.dequeue())
            elif op == "front":
                expected = mirror[0] if mirror else -1
                self.assertEqual(q.front(), expected)
            elif op == "rear":
                expected = mirror[-1] if mirror else -1
                self.assertEqual(q.rear(), expected)
            elif op == "is_empty":
                self.assertEqual(q.is_empty(), len(mirror) == 0)
            elif op == "is_full":
                self.assertEqual(q.is_full(), len(mirror) == k)
