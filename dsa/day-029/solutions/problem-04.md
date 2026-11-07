# Solution 4: Merge K Sorted Linked Lists

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** k-way-merge

## Approach

Use a min-heap to keep track of the smallest current head among all non-empty lists. Repeatedly extract the minimum node, attach it to the merged list, and push its next node (if any) back into the heap.

## Thought Process

A naive approach is to collect all nodes, sort their values, and construct a new list. While that takes $O(N \log N)$ time (where $N$ is the total number of nodes), it discards the fact that each individual list is already sorted.

Another approach is merging lists sequentially (list 1 with list 2, then result with list 3, etc.), but this takes $O(k N)$ time in the worst case, which is too slow when $k$ is up to $10^4$.

Instead, at any moment during the merge, the next smallest node must be one of the heads of the remaining $k$ lists. A min-heap containing at most $k$ elements allows us to find and extract the smallest node in $O(\log k)$ time. When pushing onto the heap, we can include a unique counter index alongside the node value so that Python's `heapq` does not attempt to compare `ListNode` objects directly when values are identical.

## Algorithm

1. Initialize an empty min-heap `heap` and a counter `entry_idx = 0` to act as a tie-breaker.
2. Iterate through all heads in `lists`. If a head is not `None`, push `(head.val, entry_idx, head)` into `heap` and increment `entry_idx`.
3. Create a dummy head node `dummy = ListNode(0)` and a pointer `curr = dummy`.
4. While `heap` is not empty, pop `(val, _, node)` from `heap`.
5. Append `node` to `curr.next`, advance `curr = curr.next`.
6. If `node.next` is not `None`, push `(node.next.val, entry_idx, node.next)` into `heap` and increment `entry_idx`.
7. Return `dummy.next`.

## Complexity Analysis

- **Time:** O(N log k) where N is the total number of nodes across all lists and k is the number of lists. Each of the N nodes is pushed and popped from a heap of size at most k.
- **Space:** O(k) auxiliary space required for the heap which stores at most k nodes at any time, plus O(1) extra space for node pointers (nodes are spliced in-place).

## Edge Cases

- Empty outer list `lists = []`: the heap remains empty and `dummy.next` (which is `None`) is returned.
- List containing only `None` elements (e.g. `[[], None]`): non-empty check skips `None`, returning `None`.
- Duplicate node values across lists: handled safely by using `entry_idx` as a secondary tuple element to avoid comparing `ListNode` instances.
- Single list `k = 1`: behaves correctly by popping and pushing successive nodes along the single list.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from typing import Optional
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """Merges k sorted linked lists into one sorted linked list."""
    heap: list[tuple[int, int, ListNode]] = []
    counter = 0

    for node in lists:
        if node is not None:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next is not None:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    tail.next = None
    return dummy.next
```
