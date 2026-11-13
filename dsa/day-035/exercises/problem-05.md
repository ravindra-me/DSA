# Problem 5: Constrained Subsequence Sum with Width Limit

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Monotonic Stack/Deque with Dynamic Programming | [Day 35: Monotonic Stack](../README.md) |

## Problem Statement

Given an integer array `nums` and a positive integer `k`, return the maximum sum of a non-empty subsequence of `nums` such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]` (with `i < j`), the condition `j - i <= k` is satisfied.

## Input

nums: list[int], k: int

## Output

int

## Constraints

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Examples

**Example 1**

```text
Input:  nums = [10, 2, -10, 5, 20], k = 2
Output: 37
```

Subsequence is [10, 2, 5, 20]. Index differences are 1, 2, 1, all <= k=2. Sum = 37.

**Example 2**

```text
Input:  nums = [-1, -2, -3], k = 1
Output: -1
```

Subsequence must be non-empty, best option is [-1].

## Function Signature

```python
def constrained_subset_sum(nums: list[int], k: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Define $dp[i]$ as the max sum of a valid subsequence ending at index $i$. $dp[i] = nums[i] + \max(0, \max_{i-k \le j < i} dp[j])$. Maintain the window maximum of $dp$ values over a sliding window of size $k$ using a monotonic max-deque.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
