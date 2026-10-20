# Problem 5: Largest Rectangle in Histogram

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | monotonic-stack-over-indices | [Day 11: Arrays](../README.md) |

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

You must achieve $O(N)$ time complexity using an array index-based monotonic stack.

## Input

A list of integers `heights`.

## Output

An integer representing the maximum rectangular area possible.

## Constraints

- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

## Examples

**Example 1**

```text
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10
```

The largest rectangle is formed between heights 5 and 6 with area = 2 * 5 = 10.

**Example 2**

```text
Input:  heights = [2, 4]
Output: 4
```

The largest rectangle can either be bar 1 alone (height 4, width 1) or both bars (height 2, width 2).

## Function Signature

```python
def largest_rectangle_area(heights: list[int]) -> int:
    """Calculates the maximum rectangular area formed within a histogram in O(N) time."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a monotonic increasing stack of bar indices. When a bar shorter than the top of the stack is encountered, pop the stack and calculate the rectangle formed with the popped bar as the shortest element.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
