# Problem 5: Sum of Subarray Minimums

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Counting subarrays where each element is the minimum using PSE and NSE | [Day 12: Monotonic Stack](../README.md) |

## Problem Statement

Given an array of integers `arr`, find the sum of `min(b)`, where `b` ranges over every contiguous subarray of `arr`.

Since the answer may be large, return the answer modulo $10^9 + 7$.

*Note on duplicates:* To avoid double-counting subarrays when identical minimum elements exist, define the left boundary with strict inequality (`<`) and the right boundary with non-strict inequality (`<=`), or vice versa.

## Input

`arr: list[int]` - list of positive integers.

## Output

`int` - sum of all subarray minimums modulo 1_000_000_007.

## Constraints

- 1 <= len(arr) <= 10^5
- 1 <= arr[i] <= 3 * 10^4

## Examples

**Example 1**

```text
Input:  arr = [3, 1, 2, 4]
Output: 17
```

Subarrays: [3]->3, [1]->1, [2]->2, [4]->4, [3,1]->1, [1,2]->1, [2,4]->2, [3,1,2]->1, [1,2,4]->1, [3,1,2,4]->1. Sum = 3+1+2+4+1+1+2+1+1+1 = 17.

**Example 2**

```text
Input:  arr = [11, 81, 94, 43, 3]
Output: 444
```

Sum of minimums across all subarrays is 444 modulo 10^9 + 7.

## Function Signature

```python
def sum_subarray_mins(arr: list[int]) -> int:
    """Compute sum of all contiguous subarray minimums modulo 10^9 + 7."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use monotonic stacks to compute for each element the distance to its Previous Smaller Element (strict) and Next Smaller Element (non-strict). The total contribution is `arr[i] * left_count * right_count`. Target $O(n)$ time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
