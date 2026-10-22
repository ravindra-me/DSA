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
from problem_02 import StackQueue  # noqa: E402
# ---- End of generated header ----

class TestStackQueue(TestCase):
    def test_example_1(self) -> None:
        q = StackQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
        self.assertFalse(q.empty())
        self.assertEqual(q.pop(), 2)
        self.assertTrue(q.empty())

    def test_example_2_single_element(self) -> None:
        q = StackQueue()
        self.assertTrue(q.empty())
        q.push(10)
        self.assertFalse(q.empty())
        self.assertEqual(q.pop(), 10)
        self.assertTrue(q.empty())

    def test_consecutive_peeks(self) -> None:
        q = StackQueue()
        q.push(42)
        q.push(99)
        self.assertEqual(q.peek(), 42)
        self.assertEqual(q.peek(), 42)
        self.assertEqual(q.pop(), 42)
        self.assertEqual(q.peek(), 99)
        self.assertFalse(q.empty())

    def test_interleaved_push_and_pop(self) -> None:
        q = StackQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        q.push(3)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.pop(), 2)
        q.push(4)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(q.pop(), 4)
        self.assertTrue(q.empty())

    def test_duplicate_values_and_large_numbers(self) -> None:
        q = StackQueue()
        vals = [10**9, 10**9, 0, -5, 10**9]
        for v in vals:
            q.push(v)
        for v in vals:
            self.assertEqual(q.pop(), v)
        self.assertTrue(q.empty())

    def test_large_random_operations(self) -> None:
        import collections
        import random

        rng = random.Random(42)
        q = StackQueue()
        reference = collections.deque()

        for _ in range(1000):
            # Bias towards push if queue is empty, else mix push/pop/peek
            if not reference or rng.random() < 0.6:
                val = rng.randint(1, 10**9)
                q.push(val)
                reference.append(val)
            else:
                op = rng.choice(["pop", "peek", "empty"])
                if op == "pop":
                    self.assertEqual(q.pop(), reference.popleft())
                elif op == "peek":
                    self.assertEqual(q.peek(), reference[0])
                elif op == "empty":
                    self.assertEqual(q.empty(), len(reference) == 0)

        while reference:
            self.assertEqual(q.pop(), reference.popleft())
        self.assertTrue(q.empty())
