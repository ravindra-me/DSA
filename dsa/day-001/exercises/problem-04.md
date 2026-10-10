# Problem 4: Logarithmic Peak Finder

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Logarithmic time complexity O(log n) vs linear scan O(n) | [Day 1: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

A peak element in an array is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find any peak element and return its 0-based index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = nums[n] = -inf`. In other words, an element is always considered strictly greater than an out-of-bounds neighbor.

You must design an algorithm that runs in strictly $O(\log n)$ time.

## Input

`nums: list[int]` - an array where `nums[i] != nums[i + 1]` for all valid `i`

## Output

`int` - the index of any peak element

## Constraints

- 1 <= len(nums) <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 1]
Output: 2
```

3 is a peak element and your function should return the index number 2.

**Example 2**

```text
Input:  nums = [1, 2, 1, 3, 5, 6, 4]
Output: 1
```

Index 1 (value 2) or index 5 (value 6) are both valid peaks.

**Example 3**

```text
Input:  nums = [1]
Output: 0
```

Single element array: the only element is greater than its out-of-bounds neighbors.

## Function Signature

```python
def find_peak_element(nums: list[int]) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a binary search strategy comparing the midpoint with its adjacent neighbor to discard the half that is not guaranteed to contain a peak.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
