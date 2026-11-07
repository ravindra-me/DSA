# Problem 1: Partition List Around Pivot

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | pointer-partitioning | [Day 29: Linked List Techniques](../README.md) |

## Problem Statement

Given the `head` of a singly linked list and an integer `x`, partition it such that all nodes with values strictly less than `x` come before nodes with values greater than or equal to `x`.

You must preserve the original relative order of the nodes in each of the two partitions (stability).

## Input

`head: Optional[ListNode]`, `x: int`

## Output

`Optional[ListNode]` representing the head of the partitioned list.

## Constraints

- The number of nodes in the list is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= x <= 1000

## Examples

**Example 1**

```text
Input:  head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

Nodes less than 3 are [1, 2, 2]; nodes >= 3 are [4, 3, 5]. Concatenated stably.

**Example 2**

```text
Input:  head = [2, 1], x = 2
Output: [1, 2]
```

Node 1 is less than 2 and comes first.

**Example 3**

```text
Input:  head = [], x = 0
Output: []
```

Empty list edge case.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """Partition list such that nodes < x appear before nodes >= x preserving relative order."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two separate chains using dummy heads (one for `< x` and one for `>= x`), append nodes stably, and link the tail of the first to the head of the second. Remember to null-terminate the second tail.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
