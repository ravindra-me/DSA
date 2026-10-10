# Solution 2: Sorted Pair Target Sum

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Two-pointer linear scan vs quadratic brute force

## Approach

Use the two-pointer technique initialized at opposite ends of the sorted array. If the sum of the two pointed numbers is less than the target, advance the left pointer to increase the sum; if greater, decrement the right pointer to decrease the sum.

## Thought Process

A brute-force solution checks all pairs $(i, j)$ where $i < j$, requiring $O(n^2)$ time. While a hash table can reduce lookup time to $O(n)$, it consumes $O(n)$ auxiliary space and ignores the critical precondition that the array is already sorted.

Because `numbers` is sorted in non-decreasing order, we can establish monotonicity: for any indices $left < right$, increasing $left$ strictly increases or maintains `numbers[left]`, and decreasing $right$ strictly decreases or maintains `numbers[right]`.

Starting with $left = 0$ and $right = n - 1$:
- If `numbers[left] + numbers[right] == target`, we have found a valid pair.
- If `current_sum < target`, `numbers[left]` cannot pair with any valid element at index $\le right$ to reach `target` (since those elements are even smaller), so $left$ can be safely incremented.
- If `current_sum > target`, `numbers[right]` cannot pair with any valid element at index $\ge left$ to reach `target` (since those elements are even larger), so $right$ can be safely decremented.

This guarantees each comparison eliminates at least one candidate index without missing any valid pair, achieving $O(n)$ time with $O(1)$ space.

## Algorithm

1. Initialize two pointers: `left = 0` and `right = len(numbers) - 1`.
2. Loop while `left < right`.
3. Compute `current_sum = numbers[left] + numbers[right]`.
4. If `current_sum == target`, return the 1-based indices `(left + 1, right + 1)`.
5. If `current_sum < target`, increment `left` by 1.
6. If `current_sum > target`, decrement `right` by 1.
7. If the loop terminates with `left >= right`, return `None` as no pair sums to `target`.

## Complexity Analysis

- **Time:** $O(n)$ because each comparison either increments `left` or decrements `right`, examining at most $n$ elements in total.
- **Space:** $O(1)$ auxiliary space because the algorithm only maintains two integer index pointers.

## Edge Cases

- Minimum length array ($n = 2$): pointers check the single pair and terminate if unequal to target.
- Duplicate values: handles identical numbers summing to the target correctly (e.g., `[2, 2]` with target `4` returns `(1, 2)`).
- Negative numbers and zero: negative numbers do not affect the monotonicity of the sum, so the two-pointer logic works identically.
- Target cannot be formed: returns `None` once pointers cross without finding a match.
- Extreme value ranges: Python handles arbitrarily large integers, so values near $\pm 10^9$ will not overflow.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Find two numbers in a sorted list that sum to target, returning 1-based indices."""
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return (left + 1, right + 1)
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None
```
