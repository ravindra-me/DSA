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
from problem_01 import validate_stack_sequences  # noqa: E402
# ---- End of generated header ----

import random


class TestValidateStackSequences(TestCase):
    def test_example_1_valid(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 5, 3, 2, 1]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_example_2_invalid(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 3, 5, 1, 2]
        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_single_element(self):
        self.assertTrue(validate_stack_sequences([1], [1]))

    def test_negative_numbers_and_zero(self):
        pushed = [0, -1, -2, -3]
        popped = [-3, -2, -1, 0]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_immediate_pops(self):
        pushed = [1, 2, 3, 4]
        popped = [1, 2, 3, 4]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_large_valid_sequence(self):
        rng = random.Random(42)
        n = 1000
        pushed = list(range(n))
        rng.shuffle(pushed)
        
        # Simulate building a valid popped sequence
        stack = []
        popped = []
        push_idx = 0
        while push_idx < n or stack:
            if push_idx < n and (not stack or rng.choice([True, False])):
                stack.append(pushed[push_idx])
                push_idx += 1
            else:
                popped.append(stack.pop())
                
        self.assertTrue(validate_stack_sequences(pushed, popped))
