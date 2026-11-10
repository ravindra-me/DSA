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
from problem_04 import FreqStack  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter

class TestFreqStack(TestCase):
    def test_example_1(self):
        fs = FreqStack()
        for val in [5, 7, 5, 7, 4, 5]:
            fs.push(val)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 7)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 4)

    def test_example_2(self):
        fs = FreqStack()
        fs.push(1)
        fs.push(1)
        fs.push(2)
        self.assertEqual(fs.pop(), 1)
        self.assertEqual(fs.pop(), 2)

    def test_single_element(self):
        fs = FreqStack()
        fs.push(42)
        self.assertEqual(fs.pop(), 42)

    def test_zero_and_negative_numbers(self):
        fs = FreqStack()
        fs.push(0)
        fs.push(-10)
        fs.push(-10)
        fs.push(0)
        self.assertEqual(fs.pop(), 0)
        self.assertEqual(fs.pop(), -10)
        self.assertEqual(fs.pop(), -10)
        self.assertEqual(fs.pop(), 0)

    def test_interleaved_push_pop(self):
        fs = FreqStack()
        fs.push(1)
        fs.push(2)
        self.assertEqual(fs.pop(), 2)
        fs.push(1)
        self.assertEqual(fs.pop(), 1)
        self.assertEqual(fs.pop(), 1)

    def test_large_input_performance_and_correctness(self):
        fs = FreqStack()
        rng = random.Random(1337)
        elements = [rng.randint(1, 100) for _ in range(10000)]
        
        for el in elements:
            fs.push(el)
        
        counts = Counter(elements)
        popped = []
        for _ in range(len(elements)):
            val = fs.pop()
            max_c = max(counts.values())
            self.assertEqual(counts[val], max_c)
            counts[val] -= 1
            if counts[val] == 0:
                del counts[val]
            popped.append(val)
        
        self.assertEqual(len(popped), 10000)
