# Problem 1: Koko Eating Bananas

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Basic capacity/rate search on integers | [Day 30: Binary Search on the Answer](../README.md) |

## Problem Statement

Koko loves to eat bananas. There are `piles` of bananas, the $i$-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during that hour.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Input

`piles: list[int]`, `h: int`

## Output

`int`: minimum eating speed $k$

## Constraints

- 1 <= len(piles) <= 10^4
- len(piles) <= h <= 10^9
- 1 <= piles[i] <= 10^9

## Examples

**Example 1**

```text
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
```

At speed 4, Koko takes ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4) = 1 + 2 + 2 + 3 = 8 hours.

**Example 2**

```text
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

Since h equals len(piles), she must finish each pile in 1 hour, so k = max(piles) = 30.

## Function Signature

```python
def min_eating_speed(piles: list[int], h: int) -> int:
    """Return the minimum integer speed k to eat all bananas within h hours."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Binary search on speed $k$ in range $[1, \max(\text{piles})]$. The feasibility check computes total hours taken in $O(N)$ using ceiling division.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
