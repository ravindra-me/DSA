# Problem 4: Square Root and Optimal Fuel Blend

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Real-valued / continuous binary search with precision threshold | [Day 30: Binary Search on the Answer](../README.md) |

## Problem Statement

A high-performance engine burns two fuels in a blend. The engine efficiency for a blend ratio $x \in [0.0, 1.0]$ is governed by a strictly concave or continuous decreasing response function.

More fundamentally, given a positive real number `n` and an integer power `p`, find a real number $x$ such that $x^p = n$, rounded to 6 decimal places.

Additionally, implement `find_nth_root(n: float, p: int, eps: float = 1e-7) -> float` returning the $p$-th root accurate within $10^{-6}$. Handle cases where $n < 1.0$ as well as $n \ge 1.0$.

## Input

`n: float` ($n > 0$), `p: int` ($p \ge 1$)

## Output

`float`: the value $x$ such that $x^p \approx n$, accurate within $10^{-6}$

## Constraints

- 10^-6 <= n <= 10^9
- 1 <= p <= 30
- Result must satisfy |result^p - n| < 1e-5 or |result - actual| < 1e-6

## Examples

**Example 1**

```text
Input:  n = 27.0, p = 3
Output: 3.0
```

3^3 = 27.0

**Example 2**

```text
Input:  n = 0.25, p = 2
Output: 0.5
```

0.5^2 = 0.25. Notice when n < 1, the root is greater than n.

## Function Signature

```python
def find_nth_root(n: float, p: int, eps: float = 1e-7) -> float:
    """Return x such that x^p == n, accurate to within eps."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Real-valued binary search over $[\min(1.0, n), \max(1.0, n)]$. Run for a fixed number of iterations (e.g. 70-80 iterations) to guarantee precision without floating-point loop traps.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
