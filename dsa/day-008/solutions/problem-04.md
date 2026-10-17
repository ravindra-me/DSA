# Solution 4: Partition Linked List Around Pivot

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** O(N) time and O(1) auxiliary space pointer manipulation

## Approach

Maintain two separate sub-chains using dummy heads: one for nodes with values strictly less than `x`, and one for nodes with values greater than or equal to `x`. Traverse the original list node by node, append each node to the corresponding tail pointer, sever any trailing pointer from the greater-than tail to avoid cycles, and finally stitch the end of the less-than list to the beginning of the greater-than list.

## Thought Process

A naive approach might extract all values into an array, perform a stable partition, and then create new nodes or rewrite values in the linked list. While that achieves $O(N)$ time, reallocating nodes or copying to an intermediate array uses $O(N)$ auxiliary space, violating the strict $O(1)$ auxiliary space constraint.

Instead, we can reuse the existing `ListNode` objects directly in-place. Because stability is required (nodes must retain their original relative order within both partitions), we cannot swap values or use standard in-place quicksort partitioning techniques that disrupt relative order. Two pointers/dummy heads naturally preserve FIFO order for both partitions: as we advance down the original linked list, appending each encountered node to `less_tail` or `greater_tail` preserves insertion order. Finally, we attach `greater_dummy.next` to `less_tail.next` and ensure `greater_tail.next` is set to `None` to prevent cycles.

## Algorithm

1. Initialize two dummy sentinel nodes: `less_dummy = ListNode(0)` and `greater_dummy = ListNode(0)`.
2. Initialize two tail pointers: `less_tail = less_dummy` and `greater_tail = greater_dummy`.
3. Iterate through the linked list with a pointer `curr = head`.
4. For each node, compare `curr.val` with `x`. If `curr.val < x`, link `less_tail.next = curr` and update `less_tail = curr`. Otherwise, link `greater_tail.next = curr` and update `greater_tail = curr`.
5. Advance `curr = curr.next` at each step.
6. Set `greater_tail.next = None` to terminate the list and avoid cycles.
7. Connect the two partitions: `less_tail.next = greater_dummy.next`.
8. Return `less_dummy.next` as the new head.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the number of nodes in the list. Each node is visited and linked exactly once.
- **Space:** $O(1)$ auxiliary space. Only a constant number of pointer variables (`less_dummy`, `greater_dummy`, `less_tail`, `greater_tail`, `curr`) are used, with no new list nodes created.

## Edge Cases

- Empty list (`head is None`): Handled naturally; loop does not execute, `less_dummy.next` becomes `None`.
- Single-node list: The single node goes into either partition; the two partitions are stitched together properly without cycle.
- All nodes strictly less than `x`: `greater_tail` remains at `greater_dummy`, `greater_dummy.next` is `None`, so `less_tail.next` is `None`.
- All nodes greater than or equal to `x`: `less_tail` remains at `less_dummy`, `less_dummy.next` links to `greater_dummy.next`.
- Negative values and pivot values matching nodes: Condition `val < x` versus `val >= x` correctly categorizes values equal to `x` into the greater/equal partition.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None) -> None:
        self.val = val
        self.next = next


def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    """Partition a linked list around pivot x preserving relative order in O(N) time and O(1) space."""
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    less_tail = less_dummy
    greater_tail = greater_dummy

    curr = head
    while curr is not None:
        if curr.val < x:
            less_tail.next = curr
            less_tail = curr
        else:
            greater_tail.next = curr
            greater_tail = curr
        curr = curr.next

    greater_tail.next = None
    less_tail.next = greater_dummy.next
    return less_dummy.next
```
