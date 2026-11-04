# Problem 4: Add Two Numbers II (Most Significant Digit First)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Linked list processing with explicit stack or head expansion without reversal | [Day 26: Linked Lists](../README.md) |

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first, and each node contains a single digit. Add the two numbers and return the sum as a linked list. You may not modify the input lists (i.e. no reversing the original lists).

## Input

l1: Optional[ListNode], l2: Optional[ListNode]

## Output

Optional[ListNode]

## Constraints

- The number of nodes in each list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number without leading zeros except zero itself.

## Examples

**Example 1**

```text
Input:  l1 = 7 -> 2 -> 4 -> 3, l2 = 5 -> 6 -> 4
Output: 7 -> 8 -> 0 -> 7
```

7243 + 564 = 7807.

**Example 2**

```text
Input:  l1 = 0, l2 = 0
Output: 0
```

0 + 0 = 0.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def add_two_numbers_ii(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Adds two numbers represented by linked lists with MSB first."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Push values of both lists onto two stacks to process digits from least significant to most significant. Build the result list prepending nodes (head insertion). Target O(m + n) time and O(m + n) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
