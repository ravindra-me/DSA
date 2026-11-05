# Solution 5: Search in Rotated Sorted Array

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Modified binary search on a shifted/rotated sorted domain

## Approach

This problem requires a modified binary search. Even after rotation, at least one half of the array (either left or right of the midpoint) remains sorted. By checking which half is sorted, we can determine if the target lies within the range of that sorted half or if it must be in the unsorted half, allowing us to discard half the search space in each iteration.

## Thought Process

A brute-force linear scan would be O(n). To achieve O(log n), we must use binary search. The core challenge is the discontinuity introduced by the rotation. However, because the array was originally sorted, the midpoint `mid` creates two subarrays. Crucially, at least one of these two halves `[left, mid]` or `[mid, right]` must be sorted. By identifying the sorted half, we can check if the target falls within its bounds. If it does, we narrow our search to that half. If not, the target must reside in the other, potentially unsorted half. This preserves the divide-and-conquer efficiency of standard binary search.

## Algorithm

1. Initialize two pointers, `left` = 0 and `right` = len(nums) - 1.
2. While `left` <= `right`, calculate `mid` index.
3. If `nums[mid]` equals `target`, return `mid`.
4. Determine which side is sorted: if `nums[left] <= nums[mid]`, the left side is sorted.
5. If left side is sorted: check if `target` is within `[nums[left], nums[mid]]`. If so, adjust `right` to `mid - 1`; otherwise, search the right side (`left` = `mid + 1`).
6. If the right side is sorted (implicitly): check if `target` is within `[nums[mid], nums[right]]`. If so, adjust `left` to `mid + 1`; otherwise, search the left side (`right` = `mid - 1`).
7. If the loop finishes without finding the target, return -1.

## Complexity Analysis

- **Time:** O(log n) because we eliminate half the search space in each iteration of the loop.
- **Space:** O(1) because we only use a constant amount of extra space for pointers.

## Edge Cases

- Single element array: If target matches, returns 0; else -1.
- Not found: If target is not in the array, the loop completes and returns -1.
- Array with 2 elements: Handled correctly by mid-point logic and strict <= comparisons.
- Rotation at the very beginning or end: The logic still holds because the sorted check `nums[left] <= nums[mid]` correctly identifies the continuous segment.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def search_rotated(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1
```
