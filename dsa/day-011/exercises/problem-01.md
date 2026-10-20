# Problem 1: Sort Array by Parity II

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | two-pointers-invariants | [Day 11: Arrays](../README.md) |

## Problem Statement

Given an array of integers `nums` of even length where exactly half of the integers are even and half are odd, sort the array in-place so that whenever `nums[i]` is even, `i` is even, and whenever `nums[i]` is odd, `i` is odd.

You must mutate the array in-place and return it. Minimize auxiliary space to $O(1)$.

## Input

A list of integers `nums` of length $N$ ($N$ is even).

## Output

The mutated list of integers satisfying the parity index invariant.

## Constraints

- 2 <= len(nums) <= 2 * 10^4
- len(nums) is even
- 0 <= nums[i] <= 1000
- Exactly half of the integers in nums are even.

## Examples

**Example 1**

```text
Input:  nums = [4, 2, 5, 7]
Output: [4, 5, 2, 7]
```

[4, 7, 2, 5] and [2, 5, 4, 7] are also acceptable permutations.

**Example 2**

```text
Input:  nums = [2, 3]
Output: [2, 3]
```

Already properly aligned: index 0 has even, index 1 has odd.

## Function Signature

```python
def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    """Sorts array in-place such that even indices have even values and odd indices have odd values."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two pointers (one for even indices starting at 0, one for odd indices starting at 1). Advance them when indices already satisfy parity, and swap mismatched elements in O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
