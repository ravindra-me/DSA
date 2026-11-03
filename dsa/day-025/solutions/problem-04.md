# Solution 4: Longest Equal Element Sequence under Skip Constraint

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Linear scan state tracking with limited dynamic state

## Approach

To find the maximum contiguous subsegment length for any single target value allowing up to `k` non-matching elements (skips), we can track the index positions of each distinct number in `nums`. For a specific number, if we select a window of its occurrences from index `i` to index `j` in its position list, the total number of skipped elements between `nums[pos[i]]` and `nums[pos[j]]` is `(pos[j] - pos[i]) - (j - i)`. We can use a sliding window over the index lists of each number to find the max total window size `pos[j] - pos[i] + 1` such that the skipped count is $\le k$.

## Thought Process

A naive approach might try every starting index and every ending index of contiguous subarrays in `nums`, counting non-matching elements for the dominant number, taking $O(N^2)$ or $O(N^3)$ time. Alternatively, iterating over all unique elements and running a sliding window directly on `nums` takes $O(U \times N)$ where $U$ is the number of unique elements, which is $O(N^2)$ in the worst case.

To optimize, observe that a subsegment ending at `nums[pos[j]]` and starting at `nums[pos[i]]` for target value $v$ only needs to consider indices where $v$ actually appears as endpoints. Grouping all indices of each unique number allows us to run a two-pointer / sliding window on the list of positions for each unique value. For a window of positions `pos[i...j]`, the number of occurrences of $v$ is `j - i + 1`, and the total length of the subsegment in `nums` is `pos[j] - pos[i] + 1`. The number of skipped (ignored) non-matching elements inside this subsegment is `(pos[j] - pos[i] + 1) - (j - i + 1) = (pos[j] - pos[i]) - (j - i)`. Since each index in `nums` belongs to exactly one unique value's position list, the total length of all position lists combined is $N$. Sliding window on each position list takes $O(	ext{len}(	ext{pos}))$, leading to an overall time complexity of $O(N)$.

## Algorithm

1. Handle the edge case: if `nums` is empty, return 0.
2. Group indices by their values in `nums` using a hash map `val_to_indices` mapping `val -> list of indices`.
3. Initialize `max_len = 0`.
4. For each value and its list of indices `pos`:
5. Use a two-pointer sliding window with `left = 0` and `right` from `0` to `len(pos) - 1`.
6. Calculate skips used in the window `pos[left...right]` as `(pos[right] - pos[left]) - (right - left)`.
7. While skips > `k`, increment `left` to shrink the window.
8. Calculate the current valid contiguous subsegment length `pos[right] - pos[left] + 1` and update `max_len`.
9. Return `max_len`.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the length of `nums`. Grouping indices takes $O(N)$ time, and the sliding window processes each index at most twice across all position lists.
- **Space:** $O(N)$ to store the mapped indices of elements in the hash map.

## Edge Cases

- Empty input: Handled by returning 0 immediately.
- Single element array: Handled properly, returning 1.
- k = 0 (no skips allowed): Correctly finds the longest contiguous sequence of identical numbers.
- k larger than array length: Window can expand to cover all occurrences, capped by sequence boundaries.
- All elements unique: Returns 1 (or 1 + k bounded by N).

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import defaultdict

def max_equal_frequency_with_skips(nums: list[int], k: int) -> int:
    """Find length of longest contiguous subsegment of identical values with at most k skips."""
    if not nums:
        return 0
    
    n = len(nums)
    val_to_indices: dict[int, list[int]] = defaultdict(list)
    for idx, num in enumerate(nums):
        val_to_indices[num].append(idx)
    
    max_len = 0
    for pos in val_to_indices.values():
        left = 0
        for right in range(len(pos)):
            while (pos[right] - pos[left]) - (right - left) > k:
                left += 1
            matching_count = right - left + 1
            subsegment_len = min(n, matching_count + k)
            if subsegment_len > max_len:
                max_len = subsegment_len
                
    return max_len
```
