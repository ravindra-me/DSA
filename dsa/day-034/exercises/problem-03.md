# Problem 3: Sort Colors (3-Way Partitioning)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Dutch National Flag Partitioning | [Day 34: Quick Sort & Quickselect](../README.md) |

## Problem Statement

Given an array `nums` with $N$ objects colored red, white, or blue, represented by integers `0`, `1`, and `2` respectively, sort them in-place so that objects of the same color are adjacent, with the colors in the order red (`0`), white (`1`), and blue (`2`). You must solve this in $O(N)$ time and $O(1)$ extra space using a single pass.

## Input

`nums`: list[int]

## Output

`None`: Modify nums in-place.

## Constraints

- 1 <= len(nums) <= 10^5
- nums[i] is 0, 1, or 2

## Examples

**Example 1**

```text
Input:  nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

Array modified in-place.

**Example 2**

```text
Input:  nums = [2, 0, 1]
Output: [0, 1, 2]
```

Array modified in-place.

## Function Signature

```python
def sort_colors(nums: list[int]) -> None:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain three pointers: `low` (boundary for 0s), `mid` (current element), and `high` (boundary for 2s). While `mid <= high`, if `nums[mid] == 0`, swap with `low` and advance both; if `1`, advance `mid`; if `2`, swap with `high` and decrement `high`.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
