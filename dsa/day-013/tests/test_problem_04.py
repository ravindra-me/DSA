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
from problem_04 import predict_party_victory  # noqa: E402
# ---- End of generated header ----

import random

class TestPredictPartyVictory(TestCase):
    def test_example_1(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_example_2(self):
        self.assertEqual(predict_party_victory("RDD"), "Dire")

    def test_single_senator_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_senator_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_all_same_party(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_alternating_tie_breaker(self):
        # For "DDRRR", D at 0 bans R at 2, D at 1 bans R at 3, R at 4 bans D at 0.
        # Next round, D at 1 and R at 4 remain. D at 1 acts first and bans R at 4 -> Dire wins.
        self.assertEqual(predict_party_victory("DDRRR"), "Dire")

    def test_large_skewed_input(self):
        # 5000 'R's followed by 5000 'D's
        # First 5000 'R's will ban all 5000 'D's in the first pass.
        senate = "R" * 5000 + "D" * 5000
        self.assertEqual(predict_party_victory(senate), "Radiant")

    def test_large_alternating_input(self):
        # 10000 alternating "RD" -> "RDRD..."
        # Each R bans the adjacent D in round 1; Dire loses completely in round 1.
        senate = "RD" * 5000
        self.assertEqual(predict_party_victory(senate), "Radiant")
