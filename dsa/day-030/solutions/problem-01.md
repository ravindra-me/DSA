# Solution 1: Koko Eating Bananas

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Basic capacity/rate search on integers

## Approach

We binary search for the minimum eating speed $k$ within the range $[1, \max(\text{piles})]$. For any chosen speed $k$, the total hours required is $\sum \lceil p / k \rceil$. Because this total hours function is monotonically non-increasing with respect to $k$, binary search correctly finds the smallest $k$ where total hours $\le h$.

## Thought Process

A brute-force solution would test every integer speed starting from $k = 1$ up to $\max(\text{piles})$, checking if Koko can finish within $h$ hours. However, since $\max(\text{piles})$ can be up to $10^9$, checking sequentially could take $O(N \times \max(P))$ operations, which easily times out.

Notice the monotonicity: if speed $k$ is sufficient to finish in $\le h$ hours, any speed $k' > k$ will also be sufficient. If speed $k$ takes $> h$ hours, any speed $k' < k$ will also fail. This monotonic property (predicate: `can_finish(k)`) allows us to use binary search over the answer space $[1, \max(\text{piles})]$, reducing the search steps from $10^9$ to $\approx \log_2(10^9) \approx 30$.

## Algorithm

1. Define lower bound `low = 1` and upper bound `high = max(piles)`.
2. Define a predicate `can_finish(k)` which returns `True` if `sum((p + k - 1) // k for p in piles) <= h`, and `False` otherwise.
3. While `low < high`, compute midpoint `mid = (low + high) // 2`.
4. If `can_finish(mid)` is `True`, then `mid` might be the answer or the answer is smaller, so set `high = mid`.
5. If `can_finish(mid)` is `False`, speed `mid` is too slow, so set `low = mid + 1`.
6. When `low == high`, return `low`.

## Complexity Analysis

- **Time:** $O(n \log(\max(\text{piles})))$, where $n$ is the number of piles. Each iteration inspects all $n$ piles, and the binary search runs for $\lceil \log_2(\max(\text{piles})) \rceil \le 30$ iterations.
- **Space:** $O(1)$ auxiliary space, as we only maintain pointers and integer accumulators.

## Edge Cases

- len(piles) == h: Koko must eat each pile in at most 1 hour, so the minimum speed is exactly max(piles).
- Single pile (len(piles) == 1): Handled seamlessly; returns ceil(piles[0] / h).
- Large values of piles[i] up to 10^9 and h up to 10^9: Handled without integer overflow since Python supports arbitrary-precision integers.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    """Return the minimum integer speed k to eat all bananas within h hours."""
    low = 1
    high = max(piles)

    while low < high:
        mid = (low + high) // 2
        # Total hours needed at speed mid:
        # ceil(p / mid) is equivalent to (p + mid - 1) // mid
        hours_needed = sum((p + mid - 1) // mid for p in piles)
        if hours_needed <= h:
            high = mid
        else:
            low = mid + 1

    return low
```
