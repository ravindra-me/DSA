# Problem 4: Top K Frequent Elements via Bucketing

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | bucket sort by frequency | [Day 19: Frequency Counting](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You must solve this in $O(n)$ time complexity, where $n$ is the length of `nums`.

If multiple elements have the same frequency, sort ties in ascending numerical order in the returned list. The output should be sorted primarily by frequency descending, secondarily by value ascending.

## Input

An integer array `nums` and an integer `k` ($1 \le k \le$ number of unique elements).

## Output

A list of `k` integers ordered by frequency descending, then value ascending.

## Constraints

- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= number of unique elements in nums

## Examples

**Example 1**

```text
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

1 appears 3 times, 2 appears 2 times. The top 2 elements are [1, 2].

**Example 2**

```text
Input:  nums = [1], k = 1
Output: [1]
```

1 is the only element.

**Example 3**

```text
Input:  nums = [4, 1, -1, 2, -1, 2, 3], k = 2
Output: [-1, 2]
```

Frequencies: -1: 2, 2: 2, 4: 1, 1: 1, 3: 1. Top 2 with frequency 2 are -1 and 2 (sorted ascending: [-1, 2]).

## Function Signature

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements in O(n) time using bucket sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Count frequencies with a hash map, then place elements into frequency buckets where index = frequency. Scan buckets from n down to 1 to collect elements in O(n) total time.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
