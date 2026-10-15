# Problem 5: Maximum XOR of Two Numbers in an Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Bitwise prefix matching and greedy evaluation with masks | [Day 6: Bit Manipulation](../README.md) |

## Problem Statement

Given an integer array `nums`, return the maximum result of `nums[i] ^ nums[j]` where $0 \le i \le j < len(nums)$.

Your solution should run in $O(n)$ time (specifically $O(32n)$).

## Input

A list of non-negative integers `nums`.

## Output

An integer representing the maximum possible XOR value between any pair of elements.

## Constraints

- 1 <= len(nums) <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  nums = [3, 10, 5, 25, 2, 8]
Output: 28
```

The maximum result is 5 ^ 25 = 28 (00101 ^ 11001 = 11100).

**Example 2**

```text
Input:  nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
Output: 127
```

The maximum XOR obtained from any pair is 127.

**Example 3**

```text
Input:  nums = [0]
Output: 0
```

Only one element, 0 ^ 0 = 0.

## Function Signature

```python
def find_maximum_xor(nums: list[int]) -> int:
    """Return the maximum XOR value formed by any two numbers in nums."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate from the most significant bit (bit 30 down to 0), greedily building the candidate maximum prefix using a bitmask and checking prefix existence with a set exploiting `p1 ^ p2 = candidate <=> p1 ^ candidate = p2`.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
