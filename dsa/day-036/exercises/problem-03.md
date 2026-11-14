# Problem 3: Classic In-Place Heap Sort

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Full Heap Sort Algorithm | [Day 36: Heap Sort](../README.md) |

## Problem Statement

Given an array of integers `nums`, sort it in ascending order in-place using the Heap Sort algorithm. You must achieve $O(n \log n)$ time complexity and $O(1)$ auxiliary space without using Python's built-in `sort()`, `sorted()`, or `heapq` module.

## Input

`nums: list[int]` - The list of integers to sort.

## Output

None (sorts `nums` in-place).

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [12, 11, 13, 5, 6, 7]
Output: [5, 6, 7, 11, 12, 13]
```

Array sorted in ascending order.

**Example 2**

```text
Input:  nums = [1]
Output: [1]
```

Single-element array is trivially sorted.

**Example 3**

```text
Input:  nums = []
Output: []
```

Empty list is already sorted.

## Function Signature

```python
def heap_sort(nums: list[int]) -> None:
    """Sort nums in ascending order in-place using Heap Sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Build a max-heap in O(n) using bottom-up sift-down, then repeatedly swap nums[0] with nums[end] and sift-down index 0 while decrementing end from n - 1 to 1.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
