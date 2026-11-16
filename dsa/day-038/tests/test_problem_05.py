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
from problem_05 import shortest_path_elimination  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestShortestPathElimination(unittest.TestCase):
    def test_example_1(self):
        grid = [
            [0,0,0],
            [1,1,0],
            [0,0,0],
            [0,1,1],
            [0,0,0]
        ]
        k = 1
        self.assertEqual(shortest_path_elimination(grid, k), 6)

    def test_example_2(self):
        grid = [
            [0,1,1],
            [1,1,1],
            [1,0,0]
        ]
        k = 1
        self.assertEqual(shortest_path_elimination(grid, k), -1)

    def test_single_cell(self):
        self.assertEqual(shortest_path_elimination([[0]], 0), 0)
        self.assertEqual(shortest_path_elimination([[1]], 1), 0)
        self.assertEqual(shortest_path_elimination([[1]], 0), -1)

    def test_large_k_shortcut(self):
        grid = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 0]
        ]
        # m=3, n=4, distance = 5. k = 6 >= 3+4-1=6
        self.assertEqual(shortest_path_elimination(grid, 6), 5)

    def test_all_obstacles_insufficient_k(self):
        grid = [[1] * 4 for _ in range(4)]
        self.assertEqual(shortest_path_elimination(grid, 2), -1)

    def test_obstacle_at_start_and_end(self):
        grid = [
            [1, 0],
            [0, 1]
        ]
        self.assertEqual(shortest_path_elimination(grid, 2), 2)
        self.assertEqual(shortest_path_elimination(grid, 1), -1)

    def test_large_grid_performance(self):
        # 40x40 grid filled with alternating obstacles
        rng = random.Random(42)
        m, n = 40, 40
        grid = [[rng.choice([0, 1]) for _ in range(n)] for _ in range(m)]
        grid[0][0] = 0
        grid[m-1][n-1] = 0
        
        res = shortest_path_elimination(grid, 10)
        self.assertIsInstance(res, int)
