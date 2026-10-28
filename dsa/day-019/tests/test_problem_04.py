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
from problem_04 import top_k_frequent  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestTopKFrequent(TestCase):
    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual(top_k_frequent(nums, k), [1, 2])

    def test_example_2_single_element(self):
        nums = [1]
        k = 1
        self.assertEqual(top_k_frequent(nums, k), [1])

    def test_example_3_negative_and_ties(self):
        nums = [4, 1, -1, 2, -1, 2, 3]
        k = 2
        self.assertEqual(top_k_frequent(nums, k), [-1, 2])

    def test_all_same_frequency_tie_breaking(self):
        nums = [5, 2, -3, 0]
        k = 3
        # All have frequency 1. Sorted ascending: [-3, 0, 2, 5]. Top 3: [-3, 0, 2]
        self.assertEqual(top_k_frequent(nums, k), [-3, 0, 2])

    def test_all_elements_identical(self):
        nums = [7, 7, 7, 7, 7]
        k = 1
        self.assertEqual(top_k_frequent(nums, k), [7])

    def test_mixed_frequencies_with_partial_bucket_pickup(self):
        # 10 appears 4 times
        # 20 and 30 appear 3 times each
        # 40 appears 1 time
        # k = 2 -> 10 (freq 4), then 20 (freq 3, sorted before 30)
        nums = [10, 10, 10, 10, 30, 20, 30, 20, 30, 20, 40]
        k = 2
        self.assertEqual(top_k_frequent(nums, k), [10, 20])

    def test_large_input(self):
        rng = random.Random(42)
        # Create an array of size 50,000 with distinct frequencies
        nums = []
        # Construct predictable top elements: 100 has 1000 copies, 200 has 900 copies, 300 has 800 copies
        nums.extend([100] * 1000)
        nums.extend([200] * 900)
        nums.extend([300] * 800)
        # Fill rest with random elements with lower counts
        for _ in range(40000):
            nums.append(rng.randint(1000, 5000))

        # Reference calculation using standard sorting on counts
        counts = Counter(nums)
        expected = sorted(counts.keys(), key=lambda x: (-counts[x], x))[:3]
        self.assertEqual(top_k_frequent(nums, 3), expected)
