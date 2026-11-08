# Problem 2: Magnetic Force Between Balls

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Maximize the minimum distance pattern | [Day 30: Binary Search on the Answer](../README.md) |

## Problem Statement

In a universe with $n$ empty baskets located at distinct integer coordinates given by `position`, you have `m` balls. You want to distribute the `m` balls into the baskets such that the **minimum magnetic force** (absolute difference in position) between any two balls is as **large as possible**.

Given the integer array `position` and the integer `m`, return the maximum possible minimum magnetic force.

## Input

`position: list[int]`, `m: int`

## Output

`int`: maximum minimum magnetic force

## Constraints

- 2 <= len(position) <= 10^5
- 2 <= m <= len(position)
- 1 <= position[i] <= 10^9
- All values in position are distinct

## Examples

**Example 1**

```text
Input:  position = [1, 2, 3, 4, 7], m = 3
Output: 3
```

Choosing positions 1, 4, and 7 gives pairwise distances 3, 3, and 6. The minimum distance is 3.

**Example 2**

```text
Input:  position = [5, 4, 3, 2, 1, 1000000000], m = 2
Output: 999999999
```

With m = 2, we can place balls at the two extreme positions 1 and 1000000000.

## Function Signature

```python
def max_distance(position: list[int], m: int) -> int:
    """Return maximum possible minimum magnetic force between any two balls."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Sort positions first. Binary search on the minimum distance $d$ in range $[1, \max - \min]$. Greedily place balls whenever current position - last placed position >= $d$.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
