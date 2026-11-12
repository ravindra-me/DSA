# Solution 3: Sort Colors (3-Way Partitioning)

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Dutch National Flag Partitioning

## Approach

We use the Dutch National Flag 3-way partitioning algorithm by maintain three pointers: `low`, `mid`, and `high`. `nums[0...low-1]` stores 0s (red), `nums[low...mid-1]` stores 1s (white), `nums[mid...high]` contains unexamined elements, and `nums[high+1...N-1]` stores 2s (blue).

## Thought Process

A simple 2-pass solution counts the frequencies of 0s, 1s, and 2s and overwrites the array. However, to solve it in a single pass with $O(1)$ space, 3-way partitioning is optimal. We initialize `low = 0`, `mid = 0`, and `high = len(nums) - 1`. While `mid <= high`, we inspect `nums[mid]`: if it's 0, we swap it with `nums[low]` and increment both `low` and `mid`; if it's 1, we simply increment `mid`; if it's 2, we swap it with `nums[high]` and decrement `high` without advancing `mid` (since the swapped element from `high` has not been examined yet).

## Algorithm

1. Initialize pointers `low = 0`, `mid = 0`, and `high = len(nums) - 1`.
2. Loop while `mid <= high`.
3. If `nums[mid] == 0`, swap `nums[low]` and `nums[mid]`, then increment both `low` and `mid`.
4. If `nums[mid] == 1`, increment `mid`.
5. If `nums[mid] == 2`, swap `nums[mid]` and `nums[high]`, then decrement `high` (do not advance `mid`).

## Complexity Analysis

- **Time:** $O(N)$ because `mid` increments or `high` decrements at every step, taking at most $N$ operations total.
- **Space:** $O(1)$ extra space as modifications are done in-place with three index variables.

## Edge Cases

- Single element array: `mid` and `high` start equal, loop runs once, array remains valid.
- Array with all identical elements (e.g. all 0s, all 1s, or all 2s): pointers adjust correctly without out-of-bound errors.
- Already sorted array: processed seamlessly in $O(N)$ single pass.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def sort_colors(nums: list[int]) -> None:
    """Sort array of 0s, 1s, and 2s in-place using 3-way partitioning."""
    low, mid, high = 0, 0, len(nums) - 1
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
