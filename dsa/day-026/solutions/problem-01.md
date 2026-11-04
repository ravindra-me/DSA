# Solution 1: Partition List around Pivot Value

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Stable partitioning using dual dummy head chains

## Approach

Maintain two separate linked lists using dummy head nodes: one for nodes with values strictly less than `x` (`less_head`) and one for nodes with values greater than or equal to `x` (`greater_head`). Iterate through the original list, detaching each node and appending it to the appropriate chain. Finally, connect the end of the 'less' chain to the start of the 'greater' chain and terminate the 'greater' chain with `None` to prevent cycles.

## Thought Process

A naive approach might extract all values into a list, sort or partition them in an array, and rebuild a linked list or mutate the node values in place. However, mutating node values isn't always permissible, and creating new nodes or arrays consumes unnecessary $O(N)$ extra memory.

To achieve $O(1)$ extra space and preserve the relative order (stability), we can reuse the existing `ListNode` objects. By creating two dummy heads (`less_head` and `greater_head`), we avoid special-case logic for empty lists or updating the head pointer. Traversing the original list linearly ensures stability since nodes are appended to their respective sublists in the exact order they appear.

## Algorithm

1. Initialize two dummy head nodes: `less_dummy` and `greater_dummy`.
2. Maintain two pointers, `less` and `greater`, initialized to their respective dummy head nodes.
3. Iterate through the input list with a traversal pointer `curr`.
4. If `curr.val < x`, append `curr` to `less.next` and advance `less`.
5. Otherwise (`curr.val >= x`), append `curr` to `greater.next` and advance `greater`.
6. Advance `curr` to `curr.next` in each iteration step.
7. After traversal, terminate the greater list by setting `greater.next = None` to avoid creating a cycle.
8. Connect the two lists by setting `less.next = greater_dummy.next`.
9. Return `less_dummy.next`.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the number of nodes in the linked list. We visit each node exactly once.
- **Space:** $O(1)$ auxiliary space. We only re-link existing nodes using a constant number of pointers.

## Edge Cases

- Empty list (`head is None`): Handled seamlessly; both sublists stay empty and `None` is returned.
- Single node: Correctly assigned to either 'less' or 'greater' sublist and returned.
- All elements strictly smaller than `x`: The 'greater' list remains empty; `less.next` receives `greater_dummy.next` which is `None`.
- All elements greater than or equal to `x`: The 'less' list remains empty; `less_dummy.next` connects directly to `greater_dummy.next`.
- List containing cycles if end of 'greater' list is not set to `None`: Explicitly mitigated by setting `greater.next = None`.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    """Partition list such that nodes < x precede nodes >= x stably."""
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    
    less = less_dummy
    greater = greater_dummy
    curr = head
    
    while curr is not None:
        if curr.val < x:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next
    
    greater.next = None
    less.next = greater_dummy.next
    
    return less_dummy.next
```
