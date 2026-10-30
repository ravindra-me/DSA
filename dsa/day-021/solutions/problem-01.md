# Solution 1: Immutable Range Sum Query

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** 1D Prefix Sum

## Approach

Precompute a prefix sum array of size $n + 1$ where `prefix[i]` stores the sum of the first `i` elements. Any subsegment sum from index `left` to `right` (inclusive) can then be evaluated in $O(1)$ time as `prefix[right + 1] - prefix[left]`.

## Thought Process

A naive approach calculates the sum of elements from `left` to `right` using a loop for each call to `sum_range`. If there are $Q$ queries and each takes $O(N)$ time in the worst case, the total query time would be $O(Q \cdot N)$, which easily times out given $Q, N \le 10^5$.

Notice that repeated additions overlap. By precalculating the cumulative sums `prefix[k] = nums[0] + ... + nums[k - 1]`, any range sum can be expressed as the difference of two prefix sums: `sum(nums[left..right]) = sum(nums[0..right]) - sum(nums[0..left-1])`. Using 1-based indexing for the prefix array (with `prefix[0] = 0`) naturally handles the boundary condition where `left == 0` without needing conditional branches.

## Algorithm

1. In `__init__`, create an array `self._prefix` of length `len(nums) + 1` initialized with 0.
2. Iterate through `nums` with index `i`, setting `self._prefix[i + 1] = self._prefix[i] + nums[i]`.
3. In `sum_range(left, right)`, return `self._prefix[right + 1] - self._prefix[left]`.

## Complexity Analysis

- **Time:** $O(N)$ for `__init__` where $N$ is `len(nums)`, and $O(1)$ for each `sum_range` query.
- **Space:** $O(N)$ extra space to store the prefix sums.

## Edge Cases

- Single element array (`len(nums) == 1`): prefix array size is 2, range [0, 0] queries `prefix[1] - prefix[0]` correctly.
- `left == 0`: queries that include the first element subtract `prefix[0]` (which is 0), avoiding index-out-of-bounds.
- Full array sum (`left == 0, right == len(nums) - 1`): returns `prefix[len(nums)] - prefix[0]`, which matches the total sum.
- Negative numbers and zeroes: addition and subtraction naturally handle signed values without overflow issues in Python.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
class NumArray:
    """Range sum query data structure using a 1D prefix sum array."""

    def __init__(self, nums: list[int]) -> None:
        """Precomputes prefix sums of nums in O(N) time."""
        self._prefix: list[int] = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self._prefix[i + 1] = self._prefix[i] + val

    def sum_range(self, left: int, right: int) -> int:
        """Computes sum of nums[left..right] in O(1) time."""
        return self._prefix[right + 1] - self._prefix[left]
```
