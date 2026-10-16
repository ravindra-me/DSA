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

def list_to_array(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

def array_to_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

class TestReverseKGroup(unittest.TestCase):
    def test_example_1(self):
        head = array_to_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 2)
        self.assertEqual(list_to_array(result), [2, 1, 4, 3, 5])

    def test_example_2(self):
        head = array_to_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 3)
        self.assertEqual(list_to_array(result), [3, 2, 1, 4, 5])

    def test_k_is_one(self):
        head = array_to_list([1, 2, 3])
        result = reverse_k_group(head, 1)
        self.assertEqual(list_to_array(result), [1, 2, 3])

    def test_k_is_list_length(self):
        head = array_to_list([1, 2, 3, 4])
        result = reverse_k_group(head, 4)
        self.assertEqual(list_to_array(result), [4, 3, 2, 1])

    def test_empty_list(self):
        result = reverse_k_group(None, 2)
        self.assertIsNone(result)

    def test_single_node(self):
        head = array_to_list([1])
        result = reverse_k_group(head, 1)
        self.assertEqual(list_to_array(result), [1])

    def test_large_input(self):
        # 5000 nodes, k=2
        input_arr = list(range(5000))
        head = array_to_list(input_arr)
        result = reverse_k_group(head, 2)
        expected = []
        for i in range(0, 5000, 2):
            expected.extend([i + 1, i])
        self.assertEqual(list_to_array(result), expected)
