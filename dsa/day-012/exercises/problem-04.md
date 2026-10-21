# Problem 4: Largest Rectangle in Histogram

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Finding left and right smaller boundaries to calculate maximal area | [Day 12: Monotonic Stack](../README.md) |

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## Input

`heights: list[int]` - array of bar heights.

## Output

`int` - the maximum rectangular area possible.

## Constraints

- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

## Examples

**Example 1**

```text
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10
```

The largest rectangle is formed between heights 5 and 6 with height 5 and width 2, giving area 10.

**Example 2**

```text
Input:  heights = [2, 4]
Output: 4
```

Bar at index 1 alone has area 4 * 1 = 4.

## Function Signature

```python
def largest_rectangle_area(heights: list[int]) -> int:
    """Find the area of the largest rectangle in a histogram."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a monotonic increasing stack of bar indices. When a shorter bar is encountered, pop previous bars and compute their area using the popped bar as height and the distance between current index and the new top of stack as width. Target $O(n)$ time.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
