# Solution 1: Two Sum Target Difference

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Complement lookup via HashMap

## Approach

We need to find indices `(i, j)` such that `nums[i] - nums[j] == diff` and `i != j`, prioritizing the smallest `i`, then smallest `j`. We can pre-record every value's list of indices or keep track of the earliest index for each number. By iterating through `i` from `0` to `len(nums) - 1`, we search for the complement `nums[j] = nums[i] - diff`. To satisfy the tie-breaking condition (smallest `j`), we look up the minimum valid index `j` for that complement where `j != i`.

## Thought Process

A brute-force solution checks all pairs `(i, j)` in order of increasing `i` and then `j`, taking $O(n^2)$ time. Given $n \le 10^5$, an $O(n^2)$ search will exceed the execution time limit.

To improve this, rearrange the equation: `nums[j] = nums[i] - diff`. For a fixed `i`, the required complement value is fixed. By pre-populating a hash map mapping each distinct value in `nums` to its list of indices (or specifically the smallest indices), we can find valid `j` in $O(1)$ time.

Since indices are recorded in increasing order, the smallest `j` for any value `target = nums[i] - diff` is simply its first index, unless that index is `i` itself (which can happen when `diff == 0`). If the first index equals `i`, the second index (if present) will be the smallest valid `j != i`. Iterating `i` from `0` to `n - 1` guarantees we find the pair with the smallest `i` first, and choosing the smallest `j != i` guarantees the tie-breaking rule.

## Algorithm

1. Build a dictionary `val_to_indices` mapping each number in `nums` to a list of its indices.
2. Iterate index `i` from `0` to `len(nums) - 1`.
3. Compute the required complement value: `target = nums[i] - diff`.
4. If `target` is present in `val_to_indices`, inspect its stored indices.
5. Select the smallest index `j` from `val_to_indices[target]` such that `j != i`. Because the index list is sorted, `j` is either the first element or (if the first is `i`) the second element.
6. If such a valid `j` exists, immediately return `(i, j)` as `i` is minimized by the outer loop and `j` is the smallest valid complement index.
7. If no pair is found after scanning all `i`, return `None`.

## Complexity Analysis

- **Time:** O(n) where n is the length of nums. Building the hash map takes O(n) time, and inspecting complement indices takes O(1) time per element.
- **Space:** O(n) to store the indices of each element in the hash map.

## Edge Cases

- diff == 0: requires nums[i] == nums[j] with i != j. The complement lookup must not pick i itself, correctly falling back to another occurrence of the same value.
- Negative diff and negative values: correctly handled by standard integer arithmetic without sign issues.
- No valid pair: loops through the entire array and cleanly returns None.
- Smallest input size (len(nums) == 2): handled naturally without out-of-bound errors.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from collections import defaultdict


def find_difference_pair(nums: list[int], diff: int) -> tuple[int, int] | None:
    """Find (i, j) such that nums[i] - nums[j] == diff."""
    val_to_indices: dict[int, list[int]] = defaultdict(list)
    for idx, num in enumerate(nums):
        # We only need at most the first two indices for any value
        if len(val_to_indices[num]) < 2:
            val_to_indices[num].append(idx)

    for i, num in enumerate(nums):
        target = num - diff
        if target in val_to_indices:
            for j in val_to_indices[target]:
                if j != i:
                    return (i, j)

    return None
```
