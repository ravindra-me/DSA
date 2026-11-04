# Problem 1: Partition List around Pivot Value

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Stable partitioning using dual dummy head chains | [Day 26: Linked Lists](../README.md) |

## Problem Statement

Given the head of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`. Preserve the original relative order of the nodes in each of the two partitions.

## Input

head: Optional[ListNode], x: int

## Output

Optional[ListNode]

## Constraints

- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200

## Examples

**Example 1**

```text
Input:  head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

Nodes less than 3 are 1, 2, 2. Nodes >= 3 are 4, 3, 5.

**Example 2**

```text
Input:  head = 2 -> 1, x = 2
Output: 1 -> 2
```

1 is less than 2, placed first.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    """Partition list such that nodes < x precede nodes >= x stably."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two separate chains using dummy nodes (less_head and greater_head), append nodes appropriately, then join them and terminate the second list with None. Aim for O(n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
