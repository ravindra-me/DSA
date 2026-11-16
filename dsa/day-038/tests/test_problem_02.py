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
from problem_02 import batch_tasks  # noqa: E402
# ---- End of generated header ----

import random


class TestBatchTasks(TestCase):
    def test_example_1(self) -> None:
        tasks = [(1, "t1"), (3, "t2"), (11, "t3"), (12, "t4")]
        expected = [["t1", "t2"], ["t3", "t4"]]
        self.assertEqual(batch_tasks(3, 10, tasks), expected)

    def test_example_2_empty_input(self) -> None:
        self.assertEqual(batch_tasks(2, 5, []), [])

    def test_batch_size_one(self) -> None:
        tasks = [(10, "a"), (10, "b"), (15, "c")]
        expected = [["a"], ["b"], ["c"]]
        self.assertEqual(batch_tasks(1, 10, tasks), expected)

    def test_single_element(self) -> None:
        tasks = [(100, "task_alone")]
        self.assertEqual(batch_tasks(5, 10, tasks), [["task_alone"]])

    def test_capacity_flush_before_timeout(self) -> None:
        tasks = [(0, "1"), (2, "2"), (4, "3"), (6, "4"), (8, "5")]
        # batch_size=2: flushes [1, 2], then [3, 4], then remainder [5]
        expected = [["1", "2"], ["3", "4"], ["5"]]
        self.assertEqual(batch_tasks(2, 10, tasks), expected)

    def test_exact_timeout_boundary(self) -> None:
        # max_wait_time = 5, oldest ts = 10; at ts = 15, delta = 5 >= 5 (timeout!)
        tasks = [(10, "a"), (15, "b")]
        expected = [["a"], ["b"]]
        self.assertEqual(batch_tasks(10, 5, tasks), expected)

    def test_below_timeout_boundary(self) -> None:
        # max_wait_time = 5, oldest ts = 10; at ts = 14, delta = 4 < 5 (no timeout)
        tasks = [(10, "a"), (14, "b")]
        expected = [["a", "b"]]
        self.assertEqual(batch_tasks(10, 5, tasks), expected)

    def test_large_input_performance_and_correctness(self) -> None:
        # 10,000 tasks with consecutive timestamps
        n = 10_000
        batch_size = 50
        max_wait_time = 1_000_000  # Will only flush by capacity
        tasks = [(i, f"task_{i}") for i in range(n)]
        result = batch_tasks(batch_size, max_wait_time, tasks)
        
        self.assertEqual(len(result), n // batch_size)
        self.assertEqual(result[0], [f"task_{i}" for i in range(50)])
        self.assertEqual(result[-1], [f"task_{i}" for i in range(n - 50, n)])
