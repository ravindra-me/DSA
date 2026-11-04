# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import ListNode, reverse_between  # noqa: E402
# ---- End of generated header ----

def list_to_array(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def array_to_list(arr: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

class TestReverseBetween(TestCase):
    def test_example_1(self):
        head = array_to_list([1, 2, 3, 4, 5])
        res = reverse_between(head, 2, 4)
        self.assertEqual(list_to_array(res), [1, 4, 3, 2, 5])

    def test_example_2(self):
        head = array_to_list([5])
        res = reverse_between(head, 1, 1)
        self.assertEqual(list_to_array(res), [5])

    def test_empty_list(self):
        res = reverse_between(None, 1, 1)
        self.assertIsNone(res)

    def test_reverse_entire_list(self):
        head = array_to_list([1, 2, 3, 4])
        res = reverse_between(head, 1, 4)
        self.assertEqual(list_to_array(res), [4, 3, 2, 1])

    def test_reverse_head_portion(self):
        head = array_to_list([10, 20, 30, 40])
        res = reverse_between(head, 1, 3)
        self.assertEqual(list_to_array(res), [30, 20, 10, 40])

    def test_reverse_tail_portion(self):
        head = array_to_list([1, 2, 3, 4, 5])
        res = reverse_between(head, 3, 5)
        self.assertEqual(list_to_array(res), [1, 2, 5, 4, 3])

    def test_negative_values_and_duplicates(self):
        head = array_to_list([-1, 0, -1, 2, 2])
        res = reverse_between(head, 2, 4)
        self.assertEqual(list_to_array(res), [-1, 2, -1, 0, 2])

    def test_large_input(self):
        import random
        rng = random.Random(42)
        data = [rng.randint(-500, 500) for _ in range(500)]
        left, right = 100, 400
        
        head = array_to_list(data)
        res = reverse_between(head, left, right)
        
        expected_data = data[:left-1] + list(reversed(data[left-1:right])) + data[right:]
        self.assertEqual(list_to_array(res), expected_data)
