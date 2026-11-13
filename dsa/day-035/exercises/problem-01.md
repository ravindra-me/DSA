# Problem 1: Visible Mountains Count

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Next Greater Element with distance thresholding | [Day 35: Monotonic Stack](../README.md) |

## Problem Statement

Given an array of mountain heights `heights`, a mountain at index `i` can see a mountain at index `j` (`i < j`) if all heights strictly between `i` and `j` are strictly less than `min(heights[i], heights[j])`. Return an array `ans` of length `N` where `ans[i]` is the number of mountains to the right that mountain `i` can see.

## Input

heights: list[int]

## Output

list[int]

## Constraints

- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9

## Examples

**Example 1**

```text
Input:  heights = [10, 6, 8, 5, 11]
Output: [3, 1, 2, 1, 0]
```

Index 0 (10) can see 6, 8, and 11. (Cannot see past 11). Index 1 (6) can see 8. Index 2 (8) can see 5 and 11. Index 3 (5) can see 11. Index 4 (11) sees nothing to its right.

**Example 2**

```text
Input:  heights = [5, 4, 3, 2, 1]
Output: [1, 1, 1, 1, 0]
```

Each mountain can only see the immediate neighbor to its right because heights are strictly decreasing.

## Function Signature

```python
def count_visible_mountains(heights: list[int]) -> list[int]:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Traverse right-to-left using a monotonic decreasing stack. When processing an element, pop strictly smaller elements from the stack (each popped mountain is visible); if the stack is not empty after popping, the remaining stack top is also visible.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
