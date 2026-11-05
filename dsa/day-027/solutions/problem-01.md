# Solution 1: Standard Binary Search

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Basic search space halving on a distinct sorted array

## Approach

Binary search maintains a search range defined by two pointers (`left` and `right`). At each step, it inspects the middle element `mid`. If `nums[mid]` equals `target`, the search is complete. If `nums[mid] < target`, the target must lie in the right half, so `left` moves to `mid + 1`. Otherwise, the target lies in the left half, so `right` moves to `mid - 1`. This process continues until `target` is found or `left > right`.

## Thought Process

A simple linear scan checks each element from left to right in $O(n)$ time. However, the problem statement guarantees that `nums` is sorted in ascending order and demands an $O(\log n)$ runtime complexity.

Because the array is sorted, comparing `target` with the median element (`nums[mid]`) allows us to immediately eliminate half of the remaining elements. Repeating this halving step reduces the search space size from $n$ to $n/2$, $n/4$, ..., down to 1 element in at most $\log_2 n$ operations.

## Algorithm

1. Initialize `left` pointer to `0` and `right` pointer to `len(nums) - 1`.
2. Loop while `left <= right`.
3. Calculate the middle index: `mid = left + (right - left) // 2` to prevent overflow in fixed-width arithmetic languages.
4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] < target`, shrink the search space to the right half by setting `left = mid + 1`.
6. If `nums[mid] > target`, shrink the search space to the left half by setting `right = mid - 1`.
7. If the loop finishes without finding `target` (`left > right`), return `-1`.

## Complexity Analysis

- **Time:** $O(\log n)$ because the search space is halved at each iteration.
- **Space:** $O(1)$ auxiliary space as only a constant number of variables (`left`, `right`, `mid`) are tracked.

## Edge Cases

- Single element array (`len(nums) == 1`): `left` and `right` start at `0`, `mid` evaluates to `0`, and correctly checks the single element.
- Target smaller than all elements or larger than all elements: `left > right` condition is triggered after logarithmic steps and returns `-1`.
- Target at the extreme ends (`nums[0]` or `nums[-1]`): handles boundaries without index out of bounds errors.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def search(nums: list[int], target: int) -> int:
    """Search target in sorted distinct list nums and return its index, or -1 if absent."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
