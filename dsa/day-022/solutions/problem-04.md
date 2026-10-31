# Solution 4: Sort Colors (Dutch National Flag)

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Three-way partitioning using multi-pointer invariants

## Approach

Maintain three pointers: `low`, `mid`, and `high` to divide the array into four regions: `nums[0:low]` contains all `0`s, `nums[low:mid]` contains all `1`s, `nums[mid:high+1]` contains unexamined elements, and `nums[high+1:]` contains all `2`s. Iterating while `mid <= high`, swap elements into their respective zones in a single pass.

## Thought Process

A naive approach is to use standard sorting, taking $O(n \log n)$ time. Another approach is counting sort: count the occurrences of 0, 1, and 2 in a first pass, then overwrite the array in a second pass. While this achieves $O(n)$ time and $O(1)$ extra space, the problem requires a single-pass algorithm.

To achieve this in one pass, we can use Edsger Dijkstra's Dutch National Flag algorithm. We maintain the invariant:
- `nums[0 .. low-1]` = 0
- `nums[low .. mid-1]` = 1
- `nums[mid .. high]` = unknown
- `nums[high+1 .. n-1]` = 2

When `nums[mid] == 0`, we swap `nums[low]` and `nums[mid]` and increment both `low` and `mid` because we know the swapped-in element at `mid` is a 1 (or 0 if `low == mid`). When `nums[mid] == 1`, it is already in the correct region, so we just increment `mid`. When `nums[mid] == 2`, we swap `nums[mid]` and `nums[high]` and decrement `high`; `mid` is not incremented because the newly swapped element at `mid` has not yet been processed.

## Algorithm

1. Initialize three pointers: `low = 0`, `mid = 0`, and `high = len(nums) - 1`.
2. Loop while `mid <= high`.
3. If `nums[mid] == 0`, swap `nums[low]` and `nums[mid]`, then advance both `low += 1` and `mid += 1`.
4. If `nums[mid] == 1`, advance `mid += 1`.
5. If `nums[mid] == 2`, swap `nums[mid]` and `nums[high]`, then decrement `high -= 1` (do not advance `mid`).

## Complexity Analysis

- **Time:** O(n) where n is the length of nums. In each iteration, either `mid` increases or `high` decreases, so the loop executes at most n times.
- **Space:** O(1) extra space because swaps are performed in-place using only three index variables.

## Edge Cases

- Single element array (e.g. `[0]`, `[1]`, `[2]`): `low == mid == high == 0`, loop runs once and terminates correctly without index errors.
- Already sorted array (e.g. `[0, 1, 2]`): elements remain untouched as pointers progress cleanly.
- Reverse sorted array (e.g. `[2, 1, 0]`): elements are systematically swapped into place.
- Array with only one distinct value (e.g. all 0s, all 1s, or all 2s): invariants hold and no out-of-bounds swaps occur.
- Array with only two of the three colors (e.g. only 0s and 2s).

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def sort_colors(nums: list[int]) -> None:
    """Sort nums in-place containing 0s, 1s, and 2s using Dutch National Flag algorithm."""
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```
