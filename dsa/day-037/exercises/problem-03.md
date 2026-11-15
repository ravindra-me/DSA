# Problem 3: Radix Sort 32-bit Integers

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | LSD Radix Sort with bitwise shifts or base representation | [Day 37: Counting, Bucket & Radix Sort](../README.md) |

## Problem Statement

Implement LSD (Least Significant Digit) Radix Sort to sort a list of non-negative 32-bit integers in non-decreasing order.

Your algorithm should process chunks of bits (e.g., 8-bit or 16-bit chunks) or base-10 digits iteratively and run in $O(d \cdot (n + b))$ time where $d$ is the number of passes and $b$ is the radix base.

## Input

A list of non-negative integers `nums` where $0 \le \text{nums}[i] < 2^{31}$.

## Output

A sorted list of integers in ascending order.

## Constraints

- 0 <= len(nums) <= 10^5
- 0 <= nums[i] < 2^31

## Examples

**Example 1**

```text
Input:  nums = [170, 45, 75, 90, 802, 24, 2, 66]
Output: [2, 24, 45, 66, 75, 90, 170, 802]
```

Sorting using Radix Sort across digits.

**Example 2**

```text
Input:  nums = [0, 0, 0]
Output: [0, 0, 0]
```

All identical elements remain unchanged.

## Function Signature

```python
def radix_sort(nums: list[int]) -> list[int]:
    """Sorts non-negative integers using LSD Radix Sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Implement LSD radix sort using a base (such as 256 for byte-by-byte or 10 for decimal) using stable counting sort on each digit/byte pass.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
