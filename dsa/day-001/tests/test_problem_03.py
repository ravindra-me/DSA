# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import AmortizedQueue  # noqa: E402
# ---- End of generated header ----

import random


class TestAmortizedQueue(unittest.TestCase):
    def test_example_1(self) -> None:
        q = AmortizedQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
        self.assertFalse(q.empty())
        self.assertEqual(q.pop(), 2)
        self.assertTrue(q.empty())

    def test_example_2_single_element_lifecycle(self) -> None:
        q = AmortizedQueue()
        self.assertTrue(q.empty())
        q.push(5)
        self.assertFalse(q.empty())
        self.assertEqual(q.pop(), 5)
        self.assertTrue(q.empty())

    def test_consecutive_peeks_do_not_alter_state(self) -> None:
        q = AmortizedQueue()
        q.push(10)
        q.push(20)
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.peek(), 20)
        self.assertEqual(q.pop(), 20)
        self.assertTrue(q.empty())

    def test_interleaved_push_and_pop(self) -> None:
        q = AmortizedQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        q.push(3)
        q.push(4)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(q.pop(), 4)
        self.assertTrue(q.empty())

    def test_zero_negative_and_duplicate_values(self) -> None:
        q = AmortizedQueue()
        values = [0, -1, 0, -999, 42, 42, -1]
        for val in values:
            q.push(val)
        for val in values:
            self.assertEqual(q.pop(), val)
        self.assertTrue(q.empty())

    def test_repeated_empty_check(self) -> None:
        q = AmortizedQueue()
        self.assertTrue(q.empty())
        q.push(100)
        self.assertFalse(q.empty())
        self.assertFalse(q.empty())
        _ = q.peek()
        self.assertFalse(q.empty())
        _ = q.pop()
        self.assertTrue(q.empty())

    def test_large_random_operations_amortized_efficiency(self) -> None:
        rng = random.Random(1337)
        q = AmortizedQueue()
        model: list[int] = []
        head = 0
        num_ops = 50_000

        for _ in range(num_ops):
            can_pop = head < len(model)
            op = rng.choice(["push", "push", "pop", "peek"] if can_pop else ["push"])

            if op == "push":
                val = rng.randint(1, 1_000_000)
                model.append(val)
                q.push(val)
            elif op == "pop":
                expected = model[head]
                head += 1
                self.assertEqual(q.pop(), expected)
            else:
                self.assertEqual(q.peek(), model[head])

        while head < len(model):
            self.assertEqual(q.pop(), model[head])
            head += 1
        self.assertTrue(q.empty())
