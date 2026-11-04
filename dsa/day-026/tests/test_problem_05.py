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
from problem_05 import Node, flatten  # noqa: E402
# ---- End of generated header ----

import random
import unittest

def to_list(head: Node | None) -> list[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def verify_doubly_linked(test_case: unittest.TestCase, head: Node | None):
    curr = head
    prev = None
    while curr:
        test_case.assertIsNone(curr.child, "Child pointer must be None after flattening")
        test_case.assertEqual(curr.prev, prev, "Prev pointer mismatch")
        prev = curr
        curr = curr.next

class TestFlattenMultilevelList(unittest.TestCase):
    def test_example_1(self):
        # 1 <-> 2 <-> 3 <-> 4, 3 child: 7 <-> 8
        n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
        n1.next, n2.prev = n2, n1
        n2.next, n3.prev = n3, n2
        n3.next, n4.prev = n4, n3
        
        n7, n8 = Node(7), Node(8)
        n7.next, n8.prev = n8, n7
        n3.child = n7
        
        res = flatten(n1)
        self.assertEqual(to_list(res), [1, 2, 3, 7, 8, 4])
        verify_doubly_linked(self, res)

    def test_example_2(self):
        # 1 <-> 2, 1 child: 3
        n1, n2 = Node(1), Node(2)
        n1.next, n2.prev = n2, n1
        n3 = Node(3)
        n1.child = n3
        
        res = flatten(n1)
        self.assertEqual(to_list(res), [1, 3, 2])
        verify_doubly_linked(self, res)

    def test_empty(self):
        self.assertIsNone(flatten(None))

    def test_single_node(self):
        n1 = Node(42)
        res = flatten(n1)
        self.assertEqual(to_list(res), [42])
        verify_doubly_linked(self, res)

    def test_nested_children(self):
        # 1 -> 2 (child 3 -> 4 (child 5))
        n1, n2 = Node(1), Node(2)
        n1.next, n2.prev = n2, n1
        
        n3, n4 = Node(3), Node(4)
        n3.next, n4.prev = n4, n3
        n2.child = n3
        
        n5 = Node(5)
        n3.child = n5
        
        res = flatten(n1)
        self.assertEqual(to_list(res), [1, 2, 3, 5, 4])
        verify_doubly_linked(self, res)

    def test_child_at_tail(self):
        # 1 <-> 2, where 2 has child 3 <-> 4
        n1, n2 = Node(1), Node(2)
        n1.next, n2.prev = n2, n1
        n3, n4 = Node(3), Node(4)
        n3.next, n4.prev = n4, n3
        n2.child = n3
        
        res = flatten(n1)
        self.assertEqual(to_list(res), [1, 2, 3, 4])
        verify_doubly_linked(self, res)

    def test_large_input(self):
        rng = random.Random(42)
        nodes = [Node(i) for i in range(1000)]
        for i in range(999):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]
            if rng.random() < 0.2 and i + 10 < 1000:
                # create a child connection
                child_node = Node(10000 + i)
                nodes[i].child = child_node
        
        res = flatten(nodes[0])
        verify_doubly_linked(self, res)
