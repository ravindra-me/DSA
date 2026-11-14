# Solution 1: Validate Max-Heap Array

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Implicit Tree Representation & Max-Heap Invariant

## Approach

Iterate through all non-leaf nodes and check that each node is greater than or equal to its left and right children (if present). If any parent-child relationship violates the max-heap property, return `False`; otherwise, return `True`.

## Thought Process

In a 0-indexed binary heap array, node $i$ has its left child at index $2i + 1$ and its right child at index $2i + 2$. Nodes beyond index $(n - 2) // 2$ are leaf nodes and have no children, so we only need to verify nodes from $0$ up to $(n - 2) // 2$.

Alternatively, we can iterate over every child index $j$ from $1$ to $n - 1$ and verify that `nums[j] <= nums[(j - 1) // 2]`. This checks every parent-child edge exactly once, naturally covers both left and right children without bounds-checking child indices separately, and handles empty or single-element arrays effortlessly.

## Algorithm

1. Let $n$ be the length of `nums`.
2. If $n \le 1$, return `True` as any array of size 0 or 1 trivially satisfies the heap property.
3. Loop through each child index $j$ from $1$ up to $n - 1$.
4. Calculate the parent index as `parent = (j - 1) // 2`.
5. If `nums[j] > nums[parent]`, the max-heap invariant is violated; return `False` immediately.
6. If the loop finishes without violations, return `True`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the number of elements in `nums`. We inspect each element at most once and perform $O(1)$ operations per check.
- **Space:** $O(1)$ auxiliary space because we only use loop counter variables.

## Edge Cases

- Empty array (`nums = []`): Loop from 1 to 0 does not run; returns `True`.
- Single element (`nums = [42]`): Loop does not run; returns `True`.
- Duplicate values: Elements equal to their parent (`nums[j] == nums[parent]`) are valid in a max-heap ($nums[parent] \ge nums[j]$) and properly handled.
- Negative numbers and zero: Negative values obey the standard comparison (`-5 > -10`), which works seamlessly.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def is_valid_max_heap(nums: list[int]) -> bool:
    """Return True if nums represents a valid max-heap."""
    n = len(nums)
    for j in range(1, n):
        parent = (j - 1) // 2
        if nums[j] > nums[parent]:
            return False
    return True
```
