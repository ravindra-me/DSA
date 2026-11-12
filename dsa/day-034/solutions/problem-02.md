# Solution 2: Kth Smallest Element (Quickselect)

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Quickselect

## Approach

Quickselect is a divide-and-conquer algorithm based on Lomuto or Hoare partitioning from Quicksort. By picking a random pivot and partitioning the array into elements smaller than, equal to, and greater than the pivot, we can narrow down our search to a single partition. This reduces average time complexity to $O(N)$ because we only recurse into one half rather than both.

## Thought Process

A naive approach is to sort the array and return `nums[k-1]`, which takes $O(N \log N)$ time. To achieve $O(N)$ average time, we use Quickselect. After partitioning `nums` around a randomly chosen pivot, we know the exact position of the pivot and elements equal to it. If the target index `k - 1` falls into the bucket of elements equal to the pivot, we return the pivot immediately. Otherwise, we recursively/iteratively search only the left partition (if `k - 1` is smaller) or the right partition (if `k - 1` is larger). Randomized pivot selection prevents worst-case $O(N^2)$ time on sorted arrays.

## Algorithm

1. Convert 1-based index `k` to 0-based target index `target = k - 1`.
2. Define an iterative helper function that operates on bounds `left` and `right`.
3. Pick a random pivot index between `left` and `right` and swap the pivot element with `nums[right]`.
4. Partition `nums[left..right]` into three sections using 3-way partitioning (or standard 2-way partitioning) to handle duplicates efficiently.
5. Compare the target index with the boundaries of the partitions. Recurse or loop into the appropriate partition until the target index lies within the equal-to-pivot partition.
6. Return the pivot element.

## Complexity Analysis

- **Time:** $O(N)$ average time complexity, $O(N^2)$ worst-case time complexity (mitigated by randomized pivot selection).
- **Space:** $O(1)$ auxiliary space complexity since the Quickselect algorithm is implemented iteratively in-place.

## Edge Cases

- Single element array (`len(nums) == 1`): loop terminates immediately and returns the element.
- Duplicates in `nums`: 3-way partitioning handles duplicate elements efficiently without degrading performance.
- Negative numbers and zero: partitioned correctly by standard comparison operations.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
import random

def find_kth_smallest(nums: list[int], k: int) -> int:
    """Return the k-th smallest element in nums (1-indexed) using Quickselect."""
    target = k - 1
    left, right = 0, len(nums) - 1
    
    while left <= right:
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        
        # 3-way partitioning around pivot
        lt = left      # nums[left..lt-1] < pivot
        i = left       # nums[lt..i-1] == pivot
        gt = right     # nums[gt+1..right] > pivot
        
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        
        # Now nums[lt..gt] == pivot
        if lt <= target <= gt:
            return nums[target]
        elif target < lt:
            right = lt - 1
        else:
            left = gt + 1
            
    return -1
```
