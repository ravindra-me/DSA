# Solution 2: Split Linked List into k Consecutive Parts

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** List length computation and chunk slicing with dummy pointers

## Approach

First, measure the total length $N$ of the linked list by traversing it once. Divide $N$ by $k$ using integer division to find the base size `width = N // k` and remainder `remainder = N % k`. The first `remainder` parts will have size `width + 1`, and the remaining parts will have size `width`. Iterate through the list, severing the `next` link after each chunk to separate the parts.

## Thought Process

To divide the list as evenly as possible, we need to know its total size $N$. Without $N$, we wouldn't know how many nodes each part should contain. Once $N$ is calculated, the pigeonhole principle tells us that each of the $k$ parts must contain at least `N // k` nodes, with the remaining `N % k` extra nodes distributed one per part across the first `N % k` parts.

We traverse the list again, counting out the size for the current part, saving the pointer to the head of that part, moving to the last node of the current part, severing its `next` pointer to detach it, and repeating for all $k$ parts.

## Algorithm

1. Traverse the input list to compute its total length $N$.
2. Calculate base chunk size `width = N // k` and extra nodes `remainder = N % k`.
3. Initialize an empty list `result` of length $k$.
4. Maintain a pointer `curr` starting at `head`.
5. For each index `i` from $0$ to $k - 1$:
6. Determine current part size: `part_size = width + (1 if i < remainder else 0)`.
7. If `part_size == 0`, set `result[i] = None`.
8. Otherwise, set `result[i] = curr` and advance `curr` by `part_size - 1` steps to reach the end of the current chunk.
9. Save `next_part = curr.next`, sever `curr.next = None`, and update `curr = next_part`.
10. Return `result`.

## Complexity Analysis

- **Time:** $\mathcal{O}(N + k)$ where $N$ is the number of nodes in the list. We pass through the list twice and construct an output array of length $k$.
- **Space:** $\mathcal{O}(1)$ auxiliary space (excluding the output array of size $k$).

## Edge Cases

- Empty list (`head is None`): `N = 0`, all $k$ parts will be `None`.
- $k > N$: `width = 0`, the first $N$ parts will contain single nodes, and the remaining $k - N$ parts will be `None`.
- Large lists: Single linear pass prevents timeouts and memory overflows.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def split_list_to_parts(head: ListNode | None, k: int) -> list[ListNode | None]:
    """Splits linked list into k consecutive balanced parts."""
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    width, remainder = divmod(length, k)
    
    result: list[ListNode | None] = []
    curr = head
    
    for i in range(k):
        part_head = curr
        part_size = width + (1 if i < remainder else 0)
        
        if part_size > 0:
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        
        result.append(part_head)
        
    return result
```
