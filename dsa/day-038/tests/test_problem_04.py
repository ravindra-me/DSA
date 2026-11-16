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
from problem_04 import deck_revealed_increasing  # noqa: E402
# ---- End of generated header ----

import unittest
from collections import deque
import random

class TestDeckRevealedIncreasing(unittest.TestCase):
    def test_example_1(self):
        deck = [17, 13, 11, 2, 3, 5, 7]
        expected = [2, 13, 3, 11, 5, 17, 7]
        self.assertEqual(deck_revealed_increasing(deck), expected)

    def test_example_2(self):
        deck = [1]
        expected = [1]
        self.assertEqual(deck_revealed_increasing(deck), expected)

    def test_two_elements(self):
        deck = [10, 20]
        expected = [10, 20]
        self.assertEqual(deck_revealed_increasing(deck), expected)

    def test_three_elements(self):
        deck = [1, 2, 3]
        # Sorted deck: [1, 2, 3]
        # Queue of indices initially [0, 1, 2]
        # 1 -> index 0, queue becomes [2, 1]
        # 2 -> index 2, queue becomes [1]
        # 3 -> index 1
        # Expected result: [1, 3, 2]
        expected = [1, 3, 2]
        self.assertEqual(deck_revealed_increasing(deck), expected)

    def test_already_sorted_input(self):
        deck = [1, 2, 3, 4]
        # Sorted: [1, 2, 3, 4]
        # Queue indices: [0, 1, 2, 3]
        # 1 -> 0, q:[2, 3, 1]
        # 2 -> 2, q:[1, 3]
        # 3 -> 1, q:[3]
        # 4 -> 3
        # Res: [1, 3, 2, 4]
        self.assertEqual(deck_revealed_increasing([1, 2, 3, 4]), [1, 3, 2, 4])

    def test_simulation_verification_large(self):
        # Verification helper: simulates the process on a given arrangement
        def simulate(arr):
            q = deque(arr)
            revealed = []
            while q:
                revealed.append(q.popleft())
                if q:
                    q.append(q.popleft())
            return revealed

        rng = random.Random(42)
        deck = list(range(1, 1001))
        rng.shuffle(deck)
        
        result = deck_revealed_increasing(deck)
        self.assertEqual(simulate(result), sorted(deck))
