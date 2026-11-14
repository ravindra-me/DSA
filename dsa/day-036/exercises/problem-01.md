# Problem 1: Validate Max-Heap Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Implicit Tree Representation & Max-Heap Invariant | [Day 36: Heap Sort](../README.md) |

## Problem Statement

Given an array of integers `nums`, determine if it satisfies the max-heap property. That is, for every element at index `i`, its left child at `2*i + 1` (if present) must be $\le$ `nums[i]`, and its right child at `2*i + 2` (if present) must also be $\le$ `nums[i]`.

## Input

`nums: list[int]` - An array of integers.

## Output

`bool` - True if the array is a valid max-heap, False otherwise.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [10, 5, 8, 2, 4, 6, 7]
Output: True
```

Every parent is greater than or equal to its children.

**Example 2**

```text
Input:  nums = [10, 5, 8, 2, 9]
Output: False
```

Element at index 1 is 5, but its right child at index 4 is 9 (5 < 9).

**Example 3**

```text
Input:  nums = []
Output: True
```

An empty array vacuously satisfies the max-heap property.

## Function Signature

```python
def is_valid_max_heap(nums: list[int]) -> bool:
    """Return True if nums represents a valid max-heap."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through internal nodes up to (n // 2) - 1 and verify that parent >= left_child and parent >= right_child in O(n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
