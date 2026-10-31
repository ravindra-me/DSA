# Solution 3: Two Sum II - Input Array Is Sorted

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Opposite-direction convergent search on sorted sequences

## Approach

Use two pointers starting at opposite ends of the sorted array: `left` at the first element (index 0) and `right` at the last element (index $n - 1$). Compute their sum at each step; if the sum is too small, advance `left` to increase it; if too large, move `right` inwards to decrease it; if equal to `target`, return their 1-based indices.

## Thought Process

A brute-force solution evaluates all $O(n^2)$ pairs, which is too slow given $n \le 3 \times 10^4$. A hash map approach works in $O(n)$ time and $O(n)$ auxiliary space, but ignores the critical fact that the array is already sorted in non-decreasing order.

Because the array is sorted, we can exploit monotonicity: for any pair `(left, right)`, if `numbers[left] + numbers[right] < target`, no element to the left of `right` paired with `numbers[left]` can ever reach `target` (since those values are even smaller). Thus, `numbers[left]` cannot be part of the solution with any current candidate, and we can safely increment `left`. Symmetrically, if `numbers[left] + numbers[right] > target`, `numbers[right]` cannot pair with any valid element to the right of `left`, so we decrement `right`. This prunes the search space linearly, finding the unique pair in $O(n)$ time and $O(1)$ space.

## Algorithm

1. Initialize `left = 0` and `right = len(numbers) - 1`.
2. While `left < right`, compute `current_sum = numbers[left] + numbers[right]`.
3. If `current_sum == target`, return `[left + 1, right + 1]` (converting 0-based to 1-based indices).
4. If `current_sum < target`, increment `left` by 1 to seek a larger sum.
5. If `current_sum > target`, decrement `right` by 1 to seek a smaller sum.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `numbers`. In each iteration of the while loop, either `left` is incremented or `right` is decremented, so at most $n$ iterations occur before locating the target.
- **Space:** $O(1)$ auxiliary memory since only two integer pointers are used.

## Edge Cases

- Minimum array size ($n = 2$): Loop executes once or directly matches without boundary errors.
- Duplicate elements: Sorted duplicates (e.g. `[0, 0]` with target `0`) work correctly because `left` and `right` point to distinct indices.
- Negative numbers and zero: Negative sums and values preserve order and arithmetic signs without requiring special handling.
- Solution at extreme ends: The target may be formed by the very first and last elements, or by two adjacent elements.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """Find 1-based indices of two numbers in sorted list adding up to target."""
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []
```
