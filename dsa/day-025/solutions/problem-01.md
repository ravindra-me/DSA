# Solution 1: First Occurrence Index

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Basic sequential scan with early exit

## Approach

Iterate through the array sequentially from the beginning (index 0). Compare each element to `target`. Return the index immediately upon finding the first match. If the end of the array is reached without a match, return `-1`.

## Thought Process

Since the array is unsorted, we cannot skip elements using binary search or similar divide-and-conquer strategies. We must inspect elements one by one. To find the *first* occurrence, a left-to-right linear search is both necessary and optimal.

## Algorithm

1. Loop through the list `nums` using its indices from `0` to `len(nums) - 1`.
2. For each index `i`, check if `nums[i] == target`.
3. If equal, immediately return `i`.
4. If the loop finishes without finding `target`, return `-1`.

## Complexity Analysis

- **Time:** O(N) in the worst case, where N is the length of `nums`, as we may need to inspect every element once. Best case is O(1) if `target` is at index 0.
- **Space:** O(1) auxiliary space, as the search is performed in-place using a single loop variable.

## Edge Cases

- Empty array (`nums = []`): Loop does not execute; returns `-1` correctly.
- Single element array: Checked correctly in O(1) time.
- Target not present: Traverses entire array and returns `-1`.
- Target occurs multiple times: Early exit ensures the index of the first occurrence is returned.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def find_first_occurrence(nums: list[int], target: int) -> int:
    """Return the 0-based index of the first occurrence of target in nums, or -1 if absent."""
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1
```
