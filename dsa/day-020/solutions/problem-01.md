# Solution 1: Subarray Sum Divisibility Counter

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Modular Arithmetic with Hash Map Prefix Sums

## Approach

Track the running prefix sum modulo $k$ across the array. By modular arithmetic, if two prefix sums have the same remainder when divided by $k$, the subarray between them has a sum divisible by $k$. We can count frequencies of each remainder using a hash map or array.

## Thought Process

A naive brute-force checks all $O(n^2)$ contiguous subarrays and computes their sums in $O(n^2)$ time with prefix sums, which times out given $n = 30,000$.

Notice that the sum of a subarray `nums[i..j]` is `prefix[j] - prefix[i - 1]`. For this sum to be divisible by $k$:
`(prefix[j] - prefix[i - 1]) % k == 0`
which is equivalent to:
`prefix[j] % k == prefix[i - 1] % k`.

Therefore, every time we encounter a prefix sum with remainder $r = prefix[j] \pmod k$, any previous prefix sum that also had remainder $r$ forms a valid divisible subarray ending at index $j$. In Python, the `%` operator natively handles negative dividends appropriately by returning a result in $[0, k-1]$ (i.e. `-2 % 5 == 3`), ensuring standard mathematical modulo behavior. We initialize our remainder counts with `remainder_counts[0] = 1` to account for subarrays starting at index 0.

## Algorithm

1. Initialize `count = 0` to store the total number of valid subarrays.
2. Initialize `prefix_sum = 0` to track the running sum of elements.
3. Initialize a hash map or fixed-size array `remainder_counts` initialized with `{0: 1}` to handle subarrays that are divisible without subtracting an earlier prefix.
4. Iterate through each number `x` in `nums`.
5. Add `x` to `prefix_sum` and compute `rem = prefix_sum % k`.
6. Add the current count `remainder_counts.get(rem, 0)` to `count`.
7. Increment `remainder_counts[rem]` by 1.
8. Return `count`.

## Complexity Analysis

- **Time:** O(n) where n is the length of `nums`. We process each element once, doing O(1) hash map lookups and updates.
- **Space:** O(min(n, k)) to store the remainder frequencies in the dictionary or array.

## Edge Cases

- Single element array divisible by k: Handled correctly via remainder 0 initialized to frequency 1.
- Single element array not divisible by k: Correctly yields count 0.
- Negative numbers: Handled correctly because Python's `%` operator maps negative numbers to non-negative remainders in `[0, k - 1]`.
- All zeros: Every subarray sum is 0, which is divisible by any k; formula properly counts n*(n+1)//2 subarrays.
- Multiple subarrays overlapping with same remainder.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from collections import defaultdict

def count_subarrays_divisible(nums: list[int], k: int) -> int:
    """Return the number of continuous subarrays with sum divisible by k."""
    remainder_counts: dict[int, int] = defaultdict(int)
    remainder_counts[0] = 1
    
    running_sum = 0
    total_subarrays = 0
    
    for num in nums:
        running_sum += num
        rem = running_sum % k
        total_subarrays += remainder_counts[rem]
        remainder_counts[rem] += 1
        
    return total_subarrays
```
