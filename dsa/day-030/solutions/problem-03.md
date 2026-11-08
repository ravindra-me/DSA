# Solution 3: Split Array Largest Sum

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Minimize the maximum subarray sum (partitioning)

## Approach

We binary search for the minimum possible largest subarray sum. The search space ranges from $\max(nums)$ (since no subarray can have a sum smaller than the largest individual element) to $\sum(nums)$ (the case where $k=1$). For a candidate maximum sum $S$, a greedy check verifies whether $nums$ can be partitioned into $\le k$ contiguous subarrays where no subarray sum exceeds $S$.

## Thought Process

A brute-force or dynamic programming approach would consider partitioning points. The classic DP state `dp(i, j)` representing the minimum largest sum partitioning the first `i` elements into `j` subarrays takes $O(k \cdot n^2)$ or $O(k \cdot n)$ with optimizations, which is too slow for $n = 10^5$.

Notice the monotonicity property: if it is possible to partition the array such that no subarray exceeds sum $S$, it is also possible for any sum $S' > S$. Conversely, if $S$ is too small, no valid partition exists. This monotonic feasibility function makes the problem ideal for binary search on the answer.

To check if a candidate maximum sum `limit` is feasible:
1. Iterate through `nums` maintaining `current_sum` of the active subarray.
2. If adding the next number exceeds `limit`, close the current subarray, start a new one with the current number, and increment the count of subarrays.
3. If at any point the total number of required subarrays exceeds $k$, `limit` is infeasible.

Since elements are non-negative, greedy packing minimizes the number of subarrays needed for a given capacity limit.

## Algorithm

1. Identify lower bound `low = max(nums)` and upper bound `high = sum(nums)`.
2. Define helper `can_partition(max_sum)`: greedily accumulate elements into subarrays. Start with `count = 1` and `current_sum = 0`. For each `x` in `nums`, if `current_sum + x > max_sum`, set `count += 1` and `current_sum = x`. Return `count <= k`.
3. While `low < high`, compute `mid = low + (high - low) // 2`.
4. If `can_partition(mid)` is True, search the lower half by setting `high = mid`.
5. Otherwise, search the upper half by setting `low = mid + 1`.
6. Return `low` once `low == high`.

## Complexity Analysis

- **Time:** O(n * log(sum(nums) - max(nums))) where n is len(nums). With sum up to 10^14, log2(sum) <= 47 iterations, each taking O(n) operations, which runs well within 0.1s for n = 10^5.
- **Space:** O(1) auxiliary space as the binary search and feasibility check only use a few tracking variables.

## Edge Cases

- k == 1: the search space collapses or directly returns sum(nums).
- k == len(nums): each element is its own subarray, answer is max(nums).
- Single-element array (len(nums) == 1, k == 1): low == high initially, loop terminates immediately and returns nums[0].
- Elements with value 0: greedy accumulation handles zeros seamlessly without incrementing subarray count prematurely.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def split_array(nums: list[int], k: int) -> int:
    """Return the minimized largest sum among k contiguous subarrays."""
    low = max(nums)
    high = sum(nums)

    def can_partition(max_sum: int) -> bool:
        count = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > max_sum:
                count += 1
                current_sum = num
                if count > k:
                    return False
            else:
                current_sum += num
        return True

    while low < high:
        mid = low + (high - low) // 2
        if can_partition(mid):
            high = mid
        else:
            low = mid + 1

    return low
```
