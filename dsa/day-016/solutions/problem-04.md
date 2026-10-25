# Solution 4: Subarray Sum Divisible by K

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Prefix sum with modulo hashing

## Approach

A continuous subarray `nums[i..j]` has a sum divisible by `k` if and only if `prefix_sum[j + 1] % k == prefix_sum[i] % k`. By maintaining a running prefix sum modulo `k` and tracking the frequencies of each remainder using a hash map (or fixed-size array), we can count valid subarrays in a single pass.

## Thought Process

A brute-force solution would check all $O(N^2)$ subarrays and compute their sums, requiring $O(N^2)$ time. This will time out given $N = 10^5$.

To optimize, we observe that the sum of subarray $nums[i..j]$ is $P[j + 1] - P[i]$, where $P$ is the prefix sum array. We want $(P[j + 1] - P[i]) \pmod k = 0$, which is equivalent to $P[j + 1] \equiv P[i] \pmod k$.

Therefore, whenever we encounter a prefix sum with remainder $r$, any previously seen prefix sum with the same remainder $r$ forms a valid subarray ending at the current index. Python's `%` operator already handles negative numbers by returning a non-negative remainder in $[0, k - 1]$ (e.g., `-2 % 5 == 3`), which matches mathematical modular arithmetic. We initialize our remainder frequencies with `{0: 1}` to account for subarrays starting from index 0.

## Algorithm

1. Initialize `remainder_counts` with `{0: 1}` (or an array of size `k` with index 0 set to 1) representing the empty prefix sum.
2. Initialize `current_sum = 0` and `ans = 0`.
3. Iterate through each number `x` in `nums`.
4. Update `current_sum = (current_sum + x) % k`.
5. Add `remainder_counts[current_sum]` to `ans`.
6. Increment `remainder_counts[current_sum]` by 1.
7. Return `ans`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `nums`, as we iterate through the list once and perform O(1) hash map or array lookups.
- **Space:** O(min(N, k)) or O(k) auxiliary space to store the frequency of each remainder modulo `k`.

## Edge Cases

- Negative numbers: In Python, `(-2) % 5` naturally evaluates to `3`, so no manual normalization like `(r + k) % k` is required.
- Subarrays starting at index 0: Handled by pre-populating the frequency of remainder 0 with 1.
- Single-element arrays: Correctly evaluated against `k`.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import defaultdict


def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """Return the count of continuous subarrays with sum divisible by k."""
    remainder_counts: dict[int, int] = defaultdict(int)
    remainder_counts[0] = 1
    
    running_sum = 0
    result = 0
    
    for num in nums:
        running_sum = (running_sum + num) % k
        result += remainder_counts[running_sum]
        remainder_counts[running_sum] += 1
        
    return result
```
