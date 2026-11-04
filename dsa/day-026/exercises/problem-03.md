# Problem 3: Reverse Sub-List Between Positions

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | In-place partial list reversal with local pointer reconnection | [Day 26: Linked Lists](../README.md) |

## Problem Statement

Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` in 1-based indexing, and return the modified list.

## Input

head: Optional[ListNode], left: int, right: int

## Output

Optional[ListNode]

## Constraints

- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

## Examples

**Example 1**

```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
Output: 1 -> 4 -> 3 -> 2 -> 5
```

Sublist from index 2 to 4 (nodes 2, 3, 4) is reversed to 4, 3, 2.

**Example 2**

```text
Input:  head = 5, left = 1, right = 1
Output: 5
```

Single node sublist remains unchanged.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    """Reverses linked list nodes between left and right positions in-place."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dummy head. Advance a pointer to node `left - 1`. Reverse the segment `left` to `right` using standard local reversal or node-insertion logic in O(1) auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
