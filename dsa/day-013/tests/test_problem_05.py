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
from problem_05 import simulate_task_pipeline  # noqa: E402
# ---- End of generated header ----

import unittest

class TestSimulateTaskPipeline(unittest.TestCase):
    def test_example_1(self):
        capacity = 1
        tasks = [(0, 5), (1, 3), (2, 4), (5, 2)]
        self.assertEqual(simulate_task_pipeline(capacity, tasks), [5, 8, -1, 10])

    def test_example_2_empty(self):
        capacity = 2
        tasks = []
        self.assertEqual(simulate_task_pipeline(capacity, tasks), [])

    def test_single_task(self):
        capacity = 1
        tasks = [(10, 7)]
        self.assertEqual(simulate_task_pipeline(capacity, tasks), [17])

    def test_simultaneous_arrivals(self):
        # Multiple tasks arriving at the same timestamp
        capacity = 2
        tasks = [(0, 5), (0, 3), (0, 2), (0, 4)]
        # Task 0: runs 0..5 (busy)
        # Task 1: waits (buffer size 1/2), will run 5..8
        # Task 2: waits (buffer size 2/2), will run 8..10
        # Task 3: buffer full -> dropped (-1)
        self.assertEqual(simulate_task_pipeline(capacity, tasks), [5, 8, 10, -1])

    def test_idle_periods_between_bursts(self):
        capacity = 1
        tasks = [(0, 2), (10, 3), (11, 4), (12, 5)]
        # (0, 2) completes at 2. System idle until 10.
        # (10, 3) completes at 13.
        # (11, 4) waits, finishes at 17.
        # (12, 5) dropped (-1) as buffer already has (11, 4).
        self.assertEqual(simulate_task_pipeline(capacity, tasks), [2, 13, 17, -1])

    def test_exact_boundary_completion_and_arrival(self):
        capacity = 1
        # Task 0 finishes exactly at 5. Task 1 arrives at 5.
        # Task 0 finishes before or at 5, so worker is free when Task 1 arrives.
        tasks = [(0, 5), (5, 3)]
        self.assertEqual(simulate_task_pipeline(capacity, tasks), [5, 8])

    def test_large_input_linear_performance(self):
        # 20,000 tasks arriving every 2 units, each taking 10 units
        # capacity = 2 means queue quickly fills and tasks get dropped
        n = 20000
        capacity = 2
        tasks = [(i * 2, 10) for i in range(n)]
        res = simulate_task_pipeline(capacity, tasks)
        self.assertEqual(len(res), n)
        # First few: (0, 10)->finishes 10; (2, 10)->finishes 20; (4, 10)->finishes 30
        # At i=3 (time 6): running finishes at 10, queue has 20 and 30 -> full, dropped (-1)
        self.assertEqual(res[0], 10)
        self.assertEqual(res[1], 20)
        self.assertEqual(res[2], 30)
        self.assertEqual(res[3], -1)
