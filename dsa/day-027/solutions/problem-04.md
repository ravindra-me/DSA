# Solution 4: Find Peak Element

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Binary search on unsorted / locally sorted structure using local monotonicity

## Approach

We can treat this as a binary search problem. By examining the local slope at any index `mid`, we can determine which direction leads to a peak. If `nums[mid] < nums[mid + 1]`, we are on an upward slope, meaning a peak *must* exist to the right (possibly at the end of the array, but guaranteed to be somewhere in the range `[mid + 1, end]`). If `nums[mid] > nums[mid + 1]`, we are on a downward slope, meaning a peak *must* exist to the left (possibly at the very beginning of the array, but guaranteed to be in `[0, mid]`).

## Thought Process

A naive approach would be to scan the entire array linearly, which is $O(n)$. However, the problem asks for $O(\log n)$ and provides the guarantee that `nums[i] != nums[i + 1]`, which ensures that we never have a flat plateau. The property of the slope (increasing or decreasing) allows us to discard half the search space at each step, just like in standard binary search on sorted data, but here we are performing binary search on the *local trend* of an unsorted array.

## Algorithm

1. Initialize two pointers, `left = 0` and `right = len(nums) - 1`.
2. While `left < right`, calculate `mid = (left + right) // 2`.
3. Check the relationship between `nums[mid]` and `nums[mid + 1]`.
4. If `nums[mid] < nums[mid + 1]`, the peak must be to the right of `mid`, so update `left = mid + 1`.
5. Else (`nums[mid] > nums[mid + 1]`), the peak must be at `mid` or to the left, so update `right = mid`.
6. When the loop terminates, `left` will equal `right`, pointing to a peak element.

## Complexity Analysis

- **Time:** O(log n) because we halve the search space in each iteration.
- **Space:** O(1) as we only use a constant amount of extra space for pointers.

## Edge Cases

- Single element array: The loop condition `left < right` will be false immediately, correctly returning 0.
- Array with increasing sequence: The logic will keep moving `left` until it hits the end, returning the last index.
- Array with decreasing sequence: The logic will keep moving `right` until it hits index 0, returning 0.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def find_peak_element(nums: list[int]) -> int:
    """Finds a peak element in an array where nums[i] != nums[i+1]."""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            # We are on an upward slope; peak must be to the right
            left = mid + 1
        else:
            # We are on a downward slope; mid could be the peak
            right = mid
            
    return left
```
