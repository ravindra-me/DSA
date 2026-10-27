# Solution 1: Contains Duplicate

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Basic membership testing and seen-before pattern

## Approach

Iterate through the array while maintaining a hash set of previously encountered elements. If the current element is already present in the set, a duplicate has been found; otherwise, add it to the set. If the loop completes without finding duplicates, return `False`.

## Thought Process

A naive approach compares every pair of elements using nested loops, which takes $O(n^2)$ time and $O(1)$ extra space. Alternatively, sorting the array takes $O(n \log n)$ time, after which adjacent elements can be compared. However, we can do better in terms of time by trading a small amount of memory: a hash set provides $O(1)$ average-time lookup and insertion. By recording each seen number into a hash set as we traverse the list, we can detect duplicates immediately on first recurrence in a single pass of $O(n)$ time.

## Algorithm

1. Initialize an empty hash set called `seen`.
2. Iterate through each number `num` in `nums`.
3. If `num` is already in `seen`, return `True` immediately (early exit).
4. Otherwise, add `num` to `seen`.
5. If the loop finishes without returning, return `False` as all elements are unique.

## Complexity Analysis

- **Time:** O(n) on average, where n is the number of elements in nums, because set insertions and lookups take O(1) amortized time.
- **Space:** O(n) auxiliary space in the worst case to store up to n unique elements in the set.

## Edge Cases

- Single element array (len(nums) == 1): Loop terminates after one iteration, returning False correctly.
- All duplicate elements (e.g. [2, 2, 2]): Detects duplicate on the second element and returns True early.
- Duplicate appears at the very end of a large array: Correctly processed and returned as True.
- Negative numbers and zero: Properly hashed and handled as distinct integers.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice in nums."""
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
