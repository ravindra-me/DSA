# Problem 2: Rotate Array by K Steps

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | in-place array reversal and index wrapping | [Day 2: Arrays](../README.md) |

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. This modification must be done **in-place** with $O(1)$ extra memory.

## Input

`nums: list[int]`, `k: int`

## Output

`None`: modifies `nums` in place

## Constraints

- 1 <= len(nums) <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
```

Rotate 1 step: [7,1,2,3,4,5,6]. Rotate 2 steps: [6,7,1,2,3,4,5]. Rotate 3 steps: [5,6,7,1,2,3,4].

**Example 2**

```text
Input:  nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

Rotate 2 steps shifts elements by 2 positions.

**Example 3**

```text
Input:  nums = [1, 2], k = 4
Output: [1, 2]
```

k is a multiple of array length, resulting in the original array.

## Function Signature

```python
def rotate(nums: list[int], k: int) -> None:
    """Rotate nums to the right by k steps in-place."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Normalize k using modulo, then use a triple-reversal technique to achieve $O(n)$ time and $O(1)$ space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
