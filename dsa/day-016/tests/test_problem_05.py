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
from problem_05 import MapNode, MyHashMap  # noqa: E402
# ---- End of generated header ----

import random


class TestChainedHashMap(TestCase):
    def test_example_1_rehashing_and_lifecycle(self) -> None:
        hm = MyHashMap(2, 0.75)
        hm.put(1, 10)
        self.assertEqual(hm.capacity(), 2)
        self.assertEqual(hm.size(), 1)

        # size becomes 2, 2 / 2 = 1.0 > 0.75 -> triggers rehash to capacity 4
        hm.put(2, 20)
        self.assertEqual(hm.capacity(), 4)
        self.assertEqual(hm.size(), 2)
        self.assertEqual(hm.get(1), 10)
        self.assertEqual(hm.get(2), 20)

        self.assertTrue(hm.remove(1))
        self.assertEqual(hm.size(), 1)
        self.assertEqual(hm.get(1), -1)
        self.assertFalse(hm.remove(1))

    def test_example_2_missing_key(self) -> None:
        hm = MyHashMap(4, 0.75)
        self.assertEqual(hm.get(99), -1)
        self.assertFalse(hm.remove(99))
        self.assertEqual(hm.size(), 0)
        self.assertEqual(hm.capacity(), 4)

    def test_update_existing_key_does_not_rehash(self) -> None:
        hm = MyHashMap(4, 0.5)
        hm.put(10, 100)
        hm.put(20, 200)
        self.assertEqual(hm.size(), 2)
        self.assertEqual(hm.capacity(), 4)

        # Overwrite existing keys: capacity should remain 4, size 2
        hm.put(10, 105)
        hm.put(20, 205)
        self.assertEqual(hm.size(), 2)
        self.assertEqual(hm.capacity(), 4)
        self.assertEqual(hm.get(10), 105)
        self.assertEqual(hm.get(20), 205)

    def test_collisions_handling(self) -> None:
        hm = MyHashMap(8, 0.9)
        # 0, 8, 16, 24 all collide at bucket 0
        colliding_keys = [0, 8, 16, 24]
        for i, k in enumerate(colliding_keys):
            hm.put(k, (i + 1) * 100)

        self.assertEqual(hm.size(), 4)
        for i, k in enumerate(colliding_keys):
            self.assertEqual(hm.get(k), (i + 1) * 100)

        # Remove middle collision
        self.assertTrue(hm.remove(8))
        self.assertEqual(hm.get(8), -1)
        self.assertEqual(hm.get(0), 100)
        self.assertEqual(hm.get(16), 300)
        self.assertEqual(hm.get(24), 400)

    def test_zero_and_large_keys(self) -> None:
        hm = MyHashMap(2, 0.5)
        hm.put(0, 50)
        hm.put(10**6, 999)
        self.assertEqual(hm.get(0), 50)
        self.assertEqual(hm.get(10**6), 999)

    def test_large_random_operations_integrity(self) -> None:
        rng = random.Random(1337)
        hm = MyHashMap(8, 0.75)
        model: dict[int, int] = {}

        for _ in range(3000):
            op = rng.random()
            key = rng.randint(0, 1000)
            if op < 0.5:
                val = rng.randint(0, 10000)
                model[key] = val
                hm.put(key, val)
            elif op < 0.8:
                expected = model.get(key, -1)
                self.assertEqual(hm.get(key), expected)
            else:
                expected_removed = key in model
                if expected_removed:
                    del model[key]
                self.assertEqual(hm.remove(key), expected_removed)

            self.assertEqual(hm.size(), len(model))

        for k, v in model.items():
            self.assertEqual(hm.get(k), v)
