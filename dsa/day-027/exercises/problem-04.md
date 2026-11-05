# Problem 4: Find Peak Element

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Binary search on unsorted / locally sorted structure using local monotonicity | [Day 27: Binary Search](../README.md) |

## Problem Statement

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any** of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in $O(\log n)$ time.

## Input

A 0-indexed integer list `nums` where `nums[i] != nums[i + 1]` for all valid `i`.

## Output

An integer representing the index of any peak element.

## Constraints

- 1 <= len(nums) <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 1]
Output: 2
```

3 is a peak element and its index is 2.

**Example 2**

```text
Input:  nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

Index 5 (value 6) is a peak element. Index 1 (value 2) is also a valid peak answer.

## Function Signature

```python
def find_peak_element(nums: list[int]) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Compare `nums[mid]` with `nums[mid + 1]`. If `nums[mid] < nums[mid + 1]`, a peak must exist in the right half; otherwise, a peak exists in the left half (including `mid`). Shrink the range `[low, high]` until `low == high`.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
