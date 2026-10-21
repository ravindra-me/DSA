# Problem 1: Daily Temperatures

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Next greater element distance using a monotonic decreasing stack | [Day 12: Monotonic Stack](../README.md) |

## Problem Statement

Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the $i$-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.

## Input

`temperatures: list[int]` - list of daily integer temperatures.

## Output

`list[int]` - list of wait days for each day.

## Constraints

- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

## Examples

**Example 1**

```text
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

Day 0 is 73, next warmer is 74 at day 1 (wait 1). Day 2 is 75, next warmer is 76 at day 6 (wait 4).

**Example 2**

```text
Input:  temperatures = [90, 80, 70]
Output: [0, 0, 0]
```

Temperatures are strictly decreasing; no future day is warmer.

## Function Signature

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return the number of days until a warmer temperature."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a monotonic decreasing stack of indices. When the current temperature is warmer than the top of the stack, pop the index and calculate the distance. Target $O(n)$ time and $O(n)$ space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
