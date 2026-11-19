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
from problem_05 import min_completion_time  # noqa: E402
# ---- End of generated header ----

import random


class TestOptimalBudgetJobScheduler(TestCase):
    def test_example_1(self):
        jobs = [1, 2, 3, 4, 5]
        k = 2
        self.assertEqual(min_completion_time(jobs, k), 9)

    def test_example_2(self):
        jobs = [10, 20, 30]
        k = 3
        self.assertEqual(min_completion_time(jobs, k), 30)

    def test_single_element(self):
        jobs = [42]
        k = 1
        self.assertEqual(min_completion_time(jobs, k), 42)

    def test_empty_jobs(self):
        self.assertEqual(min_completion_time([], 1), 0)

    def test_single_worker(self):
        jobs = [5, 10, 15, 20]
        k = 1
        self.assertEqual(min_completion_time(jobs, k), 50)

    def test_all_zeros(self):
        jobs = [0, 0, 0, 0]
        k = 2
        self.assertEqual(min_completion_time(jobs, k), 0)

    def test_duplicate_values(self):
        jobs = [7, 7, 7, 7, 7, 7]
        k = 3
        # 6 items divided into 3 equal partitions of 2 items -> 7 + 7 = 14
        self.assertEqual(min_completion_time(jobs, k), 14)

    def test_large_input_linear_time_check(self):
        # 100,000 jobs of equal size
        n = 100_000
        val = 10
        jobs = [val] * n
        k = 4
        # Exact answer: each worker gets 25,000 elements * 10 = 250,000
        expected = (n // k) * val
        self.assertEqual(min_completion_time(jobs, k), expected)
