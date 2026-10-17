# Problem 4: Partition Linked List Around Pivot

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | O(N) time and O(1) auxiliary space pointer manipulation | [Day 8: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given the `head` of a singly linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

You must preserve the original relative order of the nodes in each of the two partitions (stable partition).

Constraints on complexity: Must run in $O(N)$ time and use $O(1)$ auxiliary space (do not allocate new list nodes).

## Input

`head: ListNode | None`, `x: int`

## Output

`ListNode | None`: head of the partitioned list

## Constraints

- The number of nodes in the list is in the range [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= x <= 1000

## Examples

**Example 1**

```text
Input:  head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

Nodes less than 3 are [1, 2, 2]; nodes >= 3 are [4, 3, 5]. Original relative order is preserved.

**Example 2**

```text
Input:  head = None, x = 0
Output: None
```

An empty list returns None.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None) -> None:
        self.val = val
        self.next = next

def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Splice existing nodes into two separate dummy-headed lists (less and greater-or-equal) and link them together in O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
