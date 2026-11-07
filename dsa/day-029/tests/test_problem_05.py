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
from problem_05 import ListNode, reverse_k_group  # noqa: E402
# ---- End of generated header ----

import random
from typing import List, Optional


def to_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_array(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


class TestReverseKGroup(TestCase):
    def test_example_1(self):
        head = to_linked_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 2)
        self.assertEqual(to_array(result), [2, 1, 4, 3, 5])

    def test_example_2(self):
        head = to_linked_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 3)
        self.assertEqual(to_array(result), [3, 2, 1, 4, 5])

    def test_example_3(self):
        head = to_linked_list([1, 2])
        result = reverse_k_group(head, 2)
        self.assertEqual(to_array(result), [2, 1])

    def test_single_node(self):
        head = to_linked_list([42])
        result = reverse_k_group(head, 1)
        self.assertEqual(to_array(result), [42])

    def test_k_equals_one(self):
        values = [1, 2, 3, 4, 5, 6]
        head = to_linked_list(values)
        result = reverse_k_group(head, 1)
        self.assertEqual(to_array(result), values)

    def test_k_equals_length(self):
        values = [10, 20, 30, 40]
        head = to_linked_list(values)
        result = reverse_k_group(head, 4)
        self.assertEqual(to_array(result), [40, 30, 20, 10])

    def test_k_greater_than_length(self):
        values = [1, 2, 3]
        head = to_linked_list(values)
        result = reverse_k_group(head, 5)
        self.assertEqual(to_array(result), [1, 2, 3])

    def test_with_duplicates_and_zeroes(self):
        values = [0, 0, 1, 1, 2, 2]
        head = to_linked_list(values)
        result = reverse_k_group(head, 2)
        self.assertEqual(to_array(result), [0, 0, 1, 1, 2, 2])

    def test_large_input(self):
        rng = random.Random(42)
        values = [rng.randint(0, 1000) for _ in range(5000)]
        k = 7

        # Compute expected using slice reversal
        expected = []
        for i in range(0, len(values), k):
            chunk = values[i : i + k]
            if len(chunk) == k:
                expected.extend(reversed(chunk))
            else:
                expected.extend(chunk)

        head = to_linked_list(values)
        result = reverse_k_group(head, k)
        self.assertEqual(to_array(result), expected)
