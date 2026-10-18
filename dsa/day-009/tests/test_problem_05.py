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
from problem_05 import ListNode, reorder_list  # noqa: E402
# ---- End of generated header ----

def build_list(values: list[int]) -> ListNode | None:
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head

def to_array(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def expected_reorder(values: list[int]) -> list[int]:
    n = len(values)
    if n <= 2:
        return list(values)
    res = []
    left, right = 0, n - 1
    while left <= right:
        if left == right:
            res.append(values[left])
            break
        res.append(values[left])
        res.append(values[right])
        left += 1
        right -= 1
    return res

class TestReorderList(TestCase):
    def test_empty_and_single_node(self):
        self.assertIsNone(reorder_list(None))
        single = build_list([42])
        self.assertEqual(to_array(reorder_list(single)), [42])

    def test_two_elements(self):
        head = build_list([1, 2])
        self.assertEqual(to_array(reorder_list(head)), [1, 2])

    def test_example_even_length(self):
        head = build_list([1, 2, 3, 4])
        self.assertEqual(to_array(reorder_list(head)), [1, 4, 2, 3])

    def test_example_odd_length(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_array(reorder_list(head)), [1, 5, 2, 4, 3])

    def test_negative_values_and_duplicates(self):
        values = [-5, 0, -5, 10, -20, 10]
        head = build_list(values)
        expected = expected_reorder(values)
        self.assertEqual(to_array(reorder_list(head)), expected)

    def test_large_list(self):
        import random
        rng = random.Random(1337)
        values = [rng.randint(-10**9, 10**9) for _ in range(5000)]
        head = build_list(values)
        result = reorder_list(head)
        expected = expected_reorder(values)
        self.assertEqual(to_array(result), expected)
