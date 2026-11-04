# Solution 4: Add Two Numbers II (Most Significant Digit First)

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Linked list processing with explicit stack or head expansion without reversal

## Approach

To add two numbers represented as linked lists with the Most Significant Digit (MSD) first without modifying/reversing the input lists, we can use explicit Stacks (Python lists). By pushing all node values onto stacks for both lists, we can pop them off to process the numbers from Least Significant Digit (LSD) to MSD. As we sum digits and process carries, we build the resulting linked list in reverse by creating new head nodes and linking them backward.

## Thought Process

Since addition natively happens from right to left (LSD to MSD), but our linked lists are ordered left to right (MSD to LSD), we need a way to process elements in Last-In, First-Out order without modifying the original linked list pointers. Stacks are the natural data structure for reversing traversal order. Alternatively, we could compute lengths, align the lists, use recursion to process nodes from tail to head, and manage the carry as a return value. However, the stack approach is clear, iterative, optimal, and easy to reason about.

## Algorithm

1. Traverse list `l1` and push all its node values onto stack `s1`.
2. Traverse list `l2` and push all its node values onto stack `s2`.
3. Initialize `carry = 0` and a pointer `head = None` for the result list.
4. Loop while `s1` is not empty, `s2` is not empty, or `carry > 0`.
5. Pop values from `s1` and `s2` if available (default to 0 if stack is empty), add them to `carry`.
6. Calculate the new digit `total % 10` and update `carry = total // 10`.
7. Create a new `ListNode` with the new digit, set its `.next` to `head`, and update `head` to this new node.
8. Return `head`.

## Complexity Analysis

- **Time:** O(N + M) where N and M are the lengths of l1 and l2. We traverse each input list once to push values onto stacks, and then loop at most max(N, M) + 1 times to pop values and build the result list.
- **Space:** O(N + M) auxiliary space to store the values of both lists in stacks, plus O(max(N, M)) space for the output list.

## Edge Cases

- Lists of different lengths (e.g., 7243 + 564): Stacks naturally handle length mismatches by defaulting to 0 once a stack is exhausted.
- Final carry creates an additional digit (e.g., 99 + 1 = 100): Handled because the loop condition includes `carry > 0`.
- Single element lists with zero (e.g., 0 + 0 = 0): Handled cleanly without extra leading zeros.
- One list being much longer than the other: Defaulting empty stacks to 0 cleanly propagates carries.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def add_two_numbers_ii(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Adds two numbers represented by linked lists with MSB first."""
    s1: list[int] = []
    s2: list[int] = []
    
    curr1 = l1
    while curr1:
        s1.append(curr1.val)
        curr1 = curr1.next
        
    curr2 = l2
    while curr2:
        s2.append(curr2.val)
        curr2 = curr2.next
        
    carry = 0
    head: ListNode | None = None
    
    while s1 or s2 or carry:
        val1 = s1.pop() if s1 else 0
        val2 = s2.pop() if s2 else 0
        
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10
        
        new_node = ListNode(digit, head)
        head = new_node
        
    return head
```
