# Solution 2: Search in Rotated Sorted Array

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** rotated-sorted-array

## Approach

In a rotated sorted array of distinct elements, splitting the array at any midpoint `mid` guarantees that at least one half (left `[low..mid]` or right `[mid..high]`) is strictly sorted. By determining which half is sorted, we can check if `target` falls within that half's range. If it does, we narrow our search to that half; otherwise, we search the other half.

## Thought Process

A naive search iterates through every element in $O(N)$ time. However, the problem requires $O(\log N)$ time, suggesting binary search. Even though the array is rotated, the key structural property remains: at least one half of the array relative to `mid` is completely sorted. We can identify the sorted half by comparing `nums[low]` with `nums[mid]`. If `nums[low] <= nums[mid]`, the left half `[low..mid]` is sorted. Otherwise, the right half `[mid..high]` must be sorted. Once we identify the sorted half, we check if `target` lies within its bounds. If so, we eliminate the other half; if not, we eliminate the sorted half. This preserves the binary search property, halving the search space at each step.

## Algorithm

1. Initialize two pointers `low = 0` and `high = len(nums) - 1`.
2. While `low <= high`, calculate `mid = low + (high - low) // 2`.
3. If `nums[mid] == target`, return `mid`.
4. Check if the left half `nums[low..mid]` is sorted (`nums[low] <= nums[mid]`):
5. - If sorted and `nums[low] <= target < nums[mid]`, update `high = mid - 1` (search left).
6. - Otherwise, update `low = mid + 1` (search right).
7. If the left half is not sorted, then the right half `nums[mid..high]` must be sorted:
8. - If `nums[mid] < target <= nums[high]`, update `low = mid + 1` (search right).
9. - Otherwise, update `high = mid - 1` (search left).
10. If `low > high` without finding `target`, return `-1`.

## Complexity Analysis

- **Time:** $O(\log N)$ because the search space is halved in every step.
- **Space:** $O(1)$ constant space as we only use pointers `low`, `high`, and `mid`.

## Edge Cases

- Single element array: `low` equals `high` initially; handled correctly by loop condition `low <= high`.
- Array is not rotated (pivot `k = 0` or fully sorted): handled naturally because `nums[low] <= nums[mid]` will always hold for the left half.
- Target is smaller or larger than all elements: correctly leads to returning `-1`.
- Target is at the boundary (first or last element, or at the pivot): inclusive/exclusive inequality comparisons accurately account for boundary elements.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def search_rotated(nums: list[int], target: int) -> int:
    """Return the index of target in rotated sorted array nums, or -1 if not found."""
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1
```
