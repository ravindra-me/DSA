# Problem 5: Container With Most Water

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Greedy area maximization via inward converging pointers | [Day 22: Two Pointers](../README.md) |

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Input

`height: list[int]` — heights of the vertical lines.

## Output

`int` — maximum area of water that can be contained.

## Constraints

- 2 <= len(height) <= 10^5
- 0 <= height[i] <= 10^4

## Examples

**Example 1**

```text
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
```

The lines are at index 1 (height 8) and index 8 (height 7). Width is 8 - 1 = 7. Height is min(8, 7) = 7. Area = 7 * 7 = 49.

**Example 2**

```text
Input:  height = [1, 1]
Output: 1
```

Width is 1, min height is 1. Area = 1.

**Example 3**

```text
Input:  height = [4, 3, 2, 1, 4]
Output: 16
```

Choosing index 0 and 4: width is 4, height is min(4, 4) = 4. Area = 16.

## Function Signature

```python
def max_area(height: list[int]) -> int:
    """Compute the maximum water volume a container can hold."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Place pointers at the ends. The width is maximized initially. Always advance the pointer pointing to the shorter vertical bar inward, as the shorter line limits capacity. O(n) time, O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
