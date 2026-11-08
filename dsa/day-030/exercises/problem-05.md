# Problem 5: K-th Smallest Pair Distance

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Two-pointer feasibility check inside binary search on answer | [Day 30: Binary Search on the Answer](../README.md) |

## Problem Statement

The distance of a pair of integers $(A, B)$ is defined as $|A - B|$.

Given an integer array `nums` and an integer `k`, return the $k$-th smallest distance among all pairs $(nums[i], nums[j])$ where $0 \le i < j < len(nums)$.

Note that $k$ is 1-indexed: $k = 1$ is the smallest distance.

## Input

`nums: list[int]`, `k: int`

## Output

`int`: the k-th smallest pair distance

## Constraints

- 2 <= len(nums) <= 2 * 10^4
- 0 <= nums[i] <= 10^6
- 1 <= k <= len(nums) * (len(nums) - 1) // 2

## Examples

**Example 1**

```text
Input:  nums = [1, 3, 1], k = 1
Output: 0
```

Pairs: (1,3)->2, (1,1)->0, (3,1)->2. Sorted distances: [0, 2, 2]. 1st is 0.

**Example 2**

```text
Input:  nums = [1, 1, 1], k = 2
Output: 0
```

All pair distances are 0.

**Example 3**

```text
Input:  nums = [1, 6, 1], k = 3
Output: 5
```

Pairs have distances 0, 5, 5. The 3rd smallest distance is 5.

## Function Signature

```python
def smallest_distance_pair(nums: list[int], k: int) -> int:
    """Return the k-th smallest distance among all pairs."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Sort `nums`. Binary search for the distance $d \in [0, \max - \min]$. Use a two-pointer sliding window to count how many pairs have distance $\le d$ in $O(N)$ time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
