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
from problem_02 import reverse_stack  # noqa: E402
# ---- End of generated header ----

import random


class TestReverseStack(TestCase):
    def test_example_one(self) -> None:
        stack = [1, 2, 3, 4, 5]
        reverse_stack(stack)
        self.assertEqual(stack, [5, 4, 3, 2, 1])

    def test_empty_stack(self) -> None:
        stack: list[int] = []
        reverse_stack(stack)
        self.assertEqual(stack, [])

    def test_single_element(self) -> None:
        stack = [42]
        reverse_stack(stack)
        self.assertEqual(stack, [42])

    def test_two_elements(self) -> None:
        stack = [10, 20]
        reverse_stack(stack)
        self.assertEqual(stack, [20, 10])

    def test_duplicate_values(self) -> None:
        stack = [1, 2, 2, 1, 3]
        reverse_stack(stack)
        self.assertEqual(stack, [3, 1, 2, 2, 1])

    def test_negative_and_zero(self) -> None:
        stack = [-5, 0, 15, -20, 0]
        reverse_stack(stack)
        self.assertEqual(stack, [0, -20, 15, 0, -5])

    def test_maximum_constraint_size(self) -> None:
        rng = random.Random(1337)
        original = [rng.randint(-10000, 10000) for _ in range(100)]
        stack = list(original)
        reverse_stack(stack)
        expected = list(reversed(original))
        self.assertEqual(stack, expected)
