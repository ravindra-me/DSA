# Solution 3: Find First and Last Position of Element in Sorted Array

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Boundary searching (lower bound and upper bound) with duplicate values

## Approach

We use binary search to perform two distinct lookups: one to find the first occurrence (lower bound) and one to find the last occurrence (upper bound). By customizing the binary search logic for each, we ensure that we narrow down the search space logarithmically while handling duplicate values.

## Thought Process

A brute-force linear scan would take O(n) time, which is unacceptable given the constraint of O(log n). Since the array is sorted, binary search is the optimal strategy. The challenge with duplicates is that standard binary search just returns 'an' index, not necessarily the first or last. To find the first occurrence, when we find the target, we don't stop; we narrow our search to the left half to see if an earlier occurrence exists. Similarly, for the last occurrence, we narrow our search to the right half. This effectively treats finding the boundary as finding the insertion point of the target (or target + 1).

## Algorithm

1. 1. Define a helper function 'find_bound' that takes 'is_first' as a boolean flag.
2. 2. Inside 'find_bound', perform standard binary search using 'left' and 'right' pointers.
3. 3. If 'nums[mid] == target': if 'is_first' is True, update 'right' to 'mid - 1' to keep looking left; otherwise, update 'left' to 'mid + 1' to keep looking right.
4. 4. If 'nums[mid] < target', move 'left' to 'mid + 1'.
5. 5. If 'nums[mid] > target', move 'right' to 'mid - 1'.
6. 6. Call 'find_bound' for both the first and last position. If the first position is not found (or index out of bounds), return [-1, -1].
7. 7. Return the indices [first_index, last_index].

## Complexity Analysis

- **Time:** O(log n) because we perform two binary searches, each taking logarithmic time relative to the number of elements in the array.
- **Space:** O(1) as we only use a constant amount of extra space for pointers and variables.

## Edge Cases

- Empty array: handled by the initial check or the binary search boundary conditions returning -1.
- Target not present: handled because the binary search will never set a valid 'bound' index for the target.
- Target appearing once: the algorithm correctly identifies the same index for both first and last.
- Target appearing multiple times at start or end of array: handled by boundary logic.
- Target smaller than all elements or larger than all elements: handled by binary search returning -1 correctly.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def search_range(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first = find_bound(is_first=True)
    if first == -1:
        return [-1, -1]
    last = find_bound(is_first=False)
    
    return [first, last]
```
