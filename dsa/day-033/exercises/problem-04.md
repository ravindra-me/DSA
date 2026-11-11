# Problem 4: Count Global Inversions

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Augmenting the merge step to count cross-inversions in O(n log n) | [Day 33: Merge Sort](../README.md) |

## Problem Statement

An inversion in an array `arr` is a pair of indices `(i, j)` such that `0 <= i < j < len(arr)` and `arr[i] > arr[j]`. Given an integer array `nums`, return the total number of inversions in the array. Your solution must run in $O(n \log n)$ time.

## Input

`nums: list[int]`, an array of integers.

## Output

`int`, the total count of inverted pairs `(i, j)`.

## Constraints

- 0 <= len(nums) <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [8, 4, 2, 1]
Output: 6
```

Pairs are (8,4), (8,2), (8,1), (4,2), (4,1), (2,1). Total = 6.

**Example 2**

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: 0
```

Already sorted in ascending order; no inversions exist.

**Example 3**

```text
Input:  nums = []
Output: 0
```

Empty list has 0 inversions.

## Function Signature

```python
def count_inversions(nums: list[int]) -> int:
    """Counts the total number of inversions in nums in O(n log n) time."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Modify merge sort. While merging left and right halves, whenever an element from right is chosen because it is strictly smaller than `left[i]`, all remaining elements from `left[i]` to `left[end]` form inversions with it.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
