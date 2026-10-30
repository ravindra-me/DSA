# Solution 3: Subarray Sum Equals K

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Prefix Sum with Hash Map

## Approach

Track the running prefix sum and maintain a frequency map of all prefix sums encountered so far. At each index, any previous prefix sum equal to `current_sum - k` represents a contiguous subarray ending at the current index that sums to `k`.

## Thought Process

A brute-force solution checks all $O(n^2)$ pairs of `(start, end)` and computes their sum, running in $O(n^2)$ time. Because the array contains negative numbers and zeros, two-pointer sliding window approaches fail since expanding or shrinking the window does not monotonically increase or decrease the sum.

Notice that the sum of a contiguous subarray `nums[i..j]` is equal to `prefix_sum[j] - prefix_sum[i - 1]`. Setting this equal to $k$ gives:
$$\text{prefix\_sum}[j] - \text{prefix\_sum}[i - 1] = k \iff \text{prefix\_sum}[i - 1] = \text{prefix\_sum}[j] - k$$

As we iterate through `nums` computing the running sum $S$, we need to count how many prior prefix sums were equal to $S - k$. By storing the frequencies of seen prefix sums in a hash map, each lookup is $O(1)$, reducing the overall time complexity from $O(n^2)$ to $O(n)$.

## Algorithm

1. Initialize `count = 0` and `running_sum = 0`.
2. Initialize a hash map (or `collections.defaultdict`) `prefix_counts` with `{0: 1}` to account for subarrays starting at index 0.
3. Iterate through each number `num` in `nums`.
4. Add `num` to `running_sum`.
5. Check if `running_sum - k` exists in `prefix_counts`. If so, add its frequency to `count`.
6. Increment the frequency of `running_sum` in `prefix_counts`.
7. Return `count` after iterating through all elements.

## Complexity Analysis

- **Time:** O(n) where n is the length of `nums`. We do a single pass over the array with O(1) average-time dictionary lookups and insertions.
- **Space:** O(n) in the worst case to store up to n + 1 distinct prefix sum values in the hash map.

## Edge Cases

- k = 0 with multiple zeros: handled naturally by tracking counts; multiple prefix sums with the same value correctly increment the answer.
- Single element matching k: initialization with `{0: 1}` ensures that if `running_sum == k`, `running_sum - k == 0` is found immediately.
- Single element not matching k: returns 0 as `running_sum - k` is not found.
- Negative numbers canceling out: handled properly because prefix sums can decrease and re-encounter previous sums without issues.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    """Count the number of contiguous subarrays summing to k."""
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1
    
    current_sum = 0
    total_subarrays = 0
    
    for num in nums:
        current_sum += num
        target_prefix = current_sum - k
        if target_prefix in prefix_counts:
            total_subarrays += prefix_counts[target_prefix]
        prefix_counts[current_sum] += 1
        
    return total_subarrays
```
