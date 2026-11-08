# Solution 4: Square Root and Optimal Fuel Blend

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Real-valued / continuous binary search with precision threshold

## Approach

We perform continuous binary search on the interval $[\text{low}, \text{high}]$ where the search bounds are initialized to $[0, \max(1.0, n)]$. Because $f(x) = x^p$ is strictly monotonic for $x \ge 0$, we can compare the midpoint raised to power $p$ against $n$ and narrow the search interval by half each step until the interval width or residual error falls below the required threshold $\varepsilon$, or after a fixed number of iterations (e.g., 80 iterations for double precision).

## Thought Process

When solving $x^p = n$ for real numbers, standard integer binary search doesn't directly apply because real numbers are continuous. However, $f(x) = x^p$ is strictly increasing on $[0, \infty)$ for $p \ge 1$.

A key observation is finding the initial bounds: when $n \ge 1$, $x \le n$, so $[0, n]$ is valid. But when $0 < n < 1$, roots become larger than the number itself (e.g., $\sqrt{0.25} = 0.5 > 0.25$). Hence, the upper bound must be $\max(1.0, n)$.

For stopping conditions, comparing `high - low > eps` or running a fixed number of iterations (around 60–80 iterations) guarantees machine-level precision since $(1/2)^{80} \approx 10^{-24}$, well exceeding standard 64-bit float precision.

## Algorithm

1. Check if p == 1; if so, return float(n).
2. Initialize search boundaries: low = 0.0 and high = max(1.0, float(n)).
3. Iterate either for a fixed number of steps (e.g., 80) or while high - low > eps.
4. Compute mid = (low + high) / 2.0.
5. Compute mid_p = mid ** p. If mid_p < n, update low = mid; otherwise update high = mid.
6. Return mid.

## Complexity Analysis

- **Time:** O(log((max(1, n)) / eps) * log(p)) because each step halves the interval width and computes mid ** p in O(log p) operations. For a fixed 80 iterations, it runs in O(log p) arithmetic operations, which is O(1) with respect to n.
- **Space:** O(1) auxiliary space as only a few scalar variables are maintained.

## Edge Cases

- n < 1.0: Handled by setting the upper bound to max(1.0, n) since x > n when n < 1.
- p = 1: Immediately returns n without needing search.
- Extremes of constraints: Very large n (10^9) or very small n (10^-6) are safely bounded within 80 iterations without numeric overflow or underflow.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def find_nth_root(n: float, p: int, eps: float = 1e-7) -> float:
    """Return x such that x^p == n, accurate to within eps."""
    if p == 1:
        return float(n)

    low = 0.0
    high = max(1.0, float(n))

    # 80 iterations halves the interval by 2^80 (~1.2e24), well beyond IEEE 754 float precision
    for _ in range(80):
        mid = (low + high) / 2.0
        if mid**p < n:
            low = mid
        else:
            high = mid

    return (low + high) / 2.0
```
