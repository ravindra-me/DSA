# Solution 5: Shortest Subarray with Sum at Least K

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Prefix Sums with Monotonic Queue Optimization

## Approach

Compute prefix sums such that any subarray sum `nums[j:i]` is `prefix[i] - prefix[j]`. Maintain candidate start indices `j` in a double-ended queue (deque) in strictly increasing order of their prefix sum values. For each index `i`, pop from the front while `prefix[i] - prefix[j] >= k` to record valid subarray lengths, and pop from the back before inserting `i` whenever `prefix[i] <= prefix[deque[-1]]` to maintain monotonicity.

## Thought Process

A naive brute-force checks all pairs $(j, i)$ with $0 \le j < i \le n$, taking $O(n^2)$ time, which is too slow for $n = 10^5$. When all numbers are non-negative, prefix sums are non-decreasing and a standard sliding window / two-pointer approach works in $O(n)$. However, with negative numbers, prefix sums are not monotonic.

To optimize, observe two properties for candidates $j$ when evaluating prefix sum at $i$ ($prefix[i] - prefix[j] \ge k$):
1. **Early retirement from the front**: If index $j$ satisfies $prefix[i] - prefix[j] \ge k$, then for any future right endpoint $i' > i$, the subarray starting at $j$ would have length $i' - j > i - j$. Since we want the *shortest* subarray, $j$ can never produce a shorter valid subarray than $i - j$. Thus, once $j$ is satisfied, we can safely pop it from the front of the queue.
2. **Pruning from the back**: Suppose we have an existing candidate $j_1$ in the queue, and we encounter $i$ such that $prefix[i] \le prefix[j_1]$ (where $i > j_1$). For any future right endpoint $i'$, $prefix[i'] - prefix[i] \ge prefix[i'] - prefix[j_1]$, meaning $i$ provides an equal or greater sum difference while being strictly closer to $i'$ ($i' - i < i' - j_1$). Thus $j_1$ is strictly inferior to $i$ and can be eliminated.

These two rules naturally yield a monotonic deque where prefix sums are maintained in strictly increasing order. Every index is pushed and popped at most once, yielding $O(n)$ time.

## Algorithm

1. Construct prefix sums `prefix` of length `n + 1` where `prefix[0] = 0` and `prefix[i] = prefix[i - 1] + nums[i - 1]`.
2. Initialize `min_length = infinity` and an empty double-ended queue `q` of indices.
3. Iterate through each index `i` from `0` to `n` in `prefix`:
4. While `q` is non-empty and `prefix[i] - prefix[q[0]] >= k`, update `min_length = min(min_length, i - q.popleft())`.
5. While `q` is non-empty and `prefix[i] <= prefix[q[-1]]`, pop from the back `q.pop()`.
6. Append index `i` to the back of `q`.
7. Return `min_length` if `min_length != infinity` else `-1`.

## Complexity Analysis

- **Time:** O(n) where n is the length of `nums`. Each index from 0 to n is pushed into the deque once and popped at most once.
- **Space:** O(n) to store the prefix sum array and the deque of indices.

## Edge Cases

- No valid subarray exists: `min_length` remains `float('inf')` and returns `-1`.
- Single element array: correctly checked when `i = 1`, comparing against `prefix[0] = 0`.
- Subarray requires only 1 element with value >= k: handled immediately as `i - (i - 1) = 1`.
- All negative numbers: prefix sums strictly decrease; no pair ever reaches positive `k`, returning `-1`.
- Large positive numbers followed by large negatives: monotonicity pruning correctly drops outdated larger prefix sums.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import deque
import math

def shortest_subarray_at_least_k(nums: list[int], k: int) -> int:
    """Return the minimum length of a contiguous subarray with sum at least k, or -1."""
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    min_len = math.inf
    q: deque[int] = deque()

    for i in range(n + 1):
        # Check if the smallest prefix sums in deque can form a valid subarray
        while q and prefix[i] - prefix[q[0]] >= k:
            min_len = min(min_len, i - q.popleft())

        # Maintain strictly increasing order of prefix sums in the deque
        while q and prefix[i] <= prefix[q[-1]]:
            q.pop()

        q.append(i)

    return min_len if min_len != math.inf else -1
```
