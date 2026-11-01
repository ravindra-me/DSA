# Problem 3: Sum of Hamming Distances of All Pairs

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Bit-by-bit contribution counting across array elements | [Day 23: Bit Manipulation](../README.md) |

## Problem Statement

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an array of integers `nums`, return the sum of Hamming distances between all pairs of integers in `nums`.

Pairs are unordered: for each pair $(i, j)$ with $0 \le i < j < n$, compute the distance and sum them up.

## Input

A list of non-negative integers `nums`.

## Output

An integer representing the total sum of Hamming distances.

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [4, 14, 2]
Output: 6
```

Hamming(4, 14) = 2, Hamming(4, 2) = 2, Hamming(14, 2) = 2. Total = 6.

**Example 2**

```text
Input:  nums = [4, 14, 4]
Output: 4
```

Hamming(4, 14) = 2, Hamming(4, 4) = 0, Hamming(14, 4) = 2. Total = 4.

**Example 3**

```text
Input:  nums = [7]
Output: 0
```

A single element has no pairs.

## Function Signature

```python
def total_hamming_distance(nums: list[int]) -> int:
    """Calculate total Hamming distance across all pairs."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Analyze each bit position independently from 0 to 30. If k elements have bit 1 and n-k have bit 0, they contribute k * (n - k) to the distance.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
