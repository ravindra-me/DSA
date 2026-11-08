# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import smallest_distance_pair  # noqa: E402
# ---- End of generated header ----

import random


class TestSmallestDistancePair(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(smallest_distance_pair([1, 3, 1], 1), 0)

    def test_example_2(self) -> None:
        self.assertEqual(smallest_distance_pair([1, 1, 1], 2), 0)

    def test_example_3(self) -> None:
        self.assertEqual(smallest_distance_pair([1, 6, 1], 3), 5)

    def test_minimal_length(self) -> None:
        self.assertEqual(smallest_distance_pair([10, 2], 1), 8)

    def test_all_elements_identical(self) -> None:
        # Any pair distance is 0
        nums = [5] * 10
        self.assertEqual(smallest_distance_pair(nums, 15), 0)

    def test_strictly_increasing_sequence(self) -> None:
        # nums = [1, 2, 3, 4]
        # Distances:
        # (1,2)->1, (2,3)->1, (3,4)->1
        # (1,3)->2, (2,4)->2
        # (1,4)->3
        # Sorted distances: [1, 1, 1, 2, 2, 3]
        nums = [1, 2, 3, 4]
        expected = [1, 1, 1, 2, 2, 3]
        for i, exp in enumerate(expected, start=1):
            self.assertEqual(smallest_distance_pair(nums, i), exp)

    def test_brute_force_comparison(self) -> None:
        rng = random.Random(1337)
        nums = [rng.randint(0, 500) for _ in range(60)]
        all_distances = sorted(
            abs(nums[i] - nums[j])
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
        )
        total_pairs = len(all_distances)
        for k in [1, 2, total_pairs // 4, total_pairs // 2, total_pairs - 1, total_pairs]:
            expected = all_distances[k - 1]
            self.assertEqual(smallest_distance_pair(nums.copy(), k), expected)

    def test_large_input_performance(self) -> None:
        # 5000 elements -> 12,497,500 pairs, brute force would timeout
        rng = random.Random(42)
        nums = [rng.randint(0, 100_000) for _ in range(5000)]
        k = 5_000_000
        ans = smallest_distance_pair(nums, k)
        self.assertIsInstance(ans, int)
        self.assertGreaterEqual(ans, 0)
