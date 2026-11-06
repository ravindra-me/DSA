# Solution 3: Find Minimum in Rotated Sorted Array

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** rotated-sorted-array

## Approach

In a rotated sorted array of unique elements, the array is split into two sorted halves relative to the last element `nums[-1]`. Elements in the left part of the pivot are strictly greater than `nums[-1]`, while elements in the right part (which includes the minimum element) are less than or equal to `nums[-1]`. We can use binary search to locate the boundary of this right sorted half.

## Thought Process

A naive approach scans the array linearly in $O(N)$ time to find the minimum. However, we can do better by leveraging the partial order. By comparing the middle element `nums[mid]` with the rightmost element `nums[right]`, we can determine which side contains the minimum:
- If `nums[mid] > nums[right]`, the minimum must be strictly to the right of `mid` (i.e., in range `[mid + 1, right]`).
- If `nums[mid] <= nums[right]`, `nums[mid]` could be the minimum or the minimum lies to its left (i.e., in range `[left, mid]`).

This shrinks the search space by half in each iteration, yielding an optimal $O(\log N)$ time complexity.

## Algorithm

1. Initialize search boundaries `left = 0` and `right = len(nums) - 1`.
2. While `left < right`:
3. Compute midpoint `mid = (left + right) // 2`.
4. If `nums[mid] > nums[right]`, set `left = mid + 1`.
5. Otherwise, set `right = mid`.
6. Return `nums[left]` as the minimum element.

## Complexity Analysis

- **Time:** $O(\log N)$ because the search space is halved in each step of the binary search loop.
- **Space:** $O(1)$ auxiliary space as we only maintain pointers `left`, `right`, and `mid`.

## Edge Cases

- Single element array (e.g., `[1]`): `left < right` condition is false initially, returns `nums[0]` immediately.
- Array is not rotated (or rotated $N$ times, e.g., `[1, 2, 3]`): `nums[mid]` is always `<= nums[right]`, narrowing `right` to `left` and returning `nums[0]`.
- Two element array (e.g., `[2, 1]`): `mid = 0`, `nums[0] > nums[1]` moves `left = 1`, correctly returning `nums[1]`.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def find_min(nums: list[int]) -> int:
    """Return the minimum element in the rotated sorted array nums."""
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
```
