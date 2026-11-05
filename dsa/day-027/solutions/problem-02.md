# Solution 2: Search Insert Position

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Finding lower-bound insertion point in a sorted array

## Approach

We use binary search to find the target's index or lower-bound insertion position. By maintaining search range search boundaries `left` and `right`, we halve the search space at each step based on whether `nums[mid]` is less than `target` or greater than or equal to `target`.

## Thought Process

A linear scan through `nums` would find the insertion point in $O(n)$ time. Since `nums` is already sorted, we can improve this to $O(\log n)$ using binary search.

We want to find the smallest index `i` such that `nums[i] >= target`. If all elements are less than `target`, the insertion position is `len(nums)`.
Using standard binary search boundaries `left = 0` and `right = len(nums)` (or `right = len(nums) - 1`), whenever `nums[mid] < target`, we know the target (if present or inserted) must be at index `mid + 1` or higher, so `left = mid + 1`. Otherwise, `nums[mid] >= target`, which means `mid` could be the insertion point, but there might be a valid index further left, so we adjust `right = mid`. When `left == right`, `left` is the exact lower bound index.

## Algorithm

1. Initialize `left = 0` and `right = len(nums)`.
2. While `left < right`:
3. Calculate `mid = left + (right - left) // 2`.
4. If `nums[mid] < target`, set `left = mid + 1`.
5. Else (`nums[mid] >= target`), set `right = mid`.
6. Return `left`.

## Complexity Analysis

- **Time:** $O(\log n)$ because the search space `[left, right)` is halved in every step.
- **Space:** $O(1)$ auxiliary space as only integer pointers `left`, `right`, and `mid` are used.

## Edge Cases

- Single element array: `left` and `right` converge correctly after 0 or 1 iteration.
- Target smaller than all elements: returns index `0`.
- Target larger than all elements: returns index `len(nums)`.
- Target exists in the array: returns exact existing index.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def search_insert(nums: list[int], target: int) -> int:
    """Find target index in sorted nums or insertion point if missing."""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```
