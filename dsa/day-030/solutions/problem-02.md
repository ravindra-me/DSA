# Solution 2: Magnetic Force Between Balls

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Maximize the minimum distance pattern

## Approach

Sort the basket positions and binary search for the maximum feasible minimum distance $d$. A greedy check in $O(n)$ time determines if at least $m$ balls can be placed such that consecutive balls are at least $d$ apart.

## Thought Process

We want to maximize a minimum value, which is a classic signature for binary search on the answer (monotonic predicate).

Suppose we test a hypothetical minimum distance $d$. If it is possible to place $m$ balls with pairwise distance $\ge d$, then any smaller distance $d' < d$ is also feasible. Conversely, if $d$ is impossible, any larger distance is also impossible. This monotonicity allows binary search on the range of possible answers $[1, \max(\text{position}) - \min(\text{position})]$.

To check feasibility for a fixed $d$ efficiently: first sort `position`. We greedily place the first ball at the very first basket `position[0]`. Then we scan through `position` and place the next ball at the first basket whose distance from the last placed ball is at least $d$. Greedy selection works because placing a ball as early as possible leaves the maximum possible remaining room for subsequent balls. If we can place at least $m$ balls this way, $d$ is feasible.

## Algorithm

1. Sort `position` in non-decreasing order.
2. Define a helper function `can_place(d)`: place the first ball at `position[0]`. Iterate through `position`, placing a ball whenever `pos - last_placed >= d`. Return `True` if at least `m` balls are placed, else `False`.
3. Initialize the binary search bounds: `low = 1` (minimum possible positive distance) and `high = position[-1] - position[0]` (maximum possible distance between extreme baskets).
4. While `low <= high`: compute `mid = (low + high) // 2`. If `can_place(mid)` is true, record `ans = mid` and search the upper half `low = mid + 1`. Otherwise, search the lower half `high = mid - 1`.
5. Return `ans`.

## Complexity Analysis

- **Time:** O(n log n + n log(max_dist)) where n is len(position) and max_dist = max(position) - min(position). Sorting takes O(n log n). The binary search performs O(log(10^9)) = ~30 iterations, each scanning through n elements in O(n) time.
- **Space:** O(1) auxiliary space beyond the space required for in-place or Timsort sorting (O(n)).

## Edge Cases

- m = 2: The optimal choice is always the two extreme positions, yielding position[-1] - position[0].
- m = len(position): Every basket must hold a ball, so the answer is the minimum adjacent difference after sorting.
- Large coordinates up to 10^9: Binary search range handles values up to 10^9 in about 30 iterations without overflow.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def max_distance(position: list[int], m: int) -> int:
    """Return maximum possible minimum magnetic force between any two balls."""
    position.sort()

    def can_place(d: int) -> bool:
        count = 1
        last_pos = position[0]
        for pos in position[1:]:
            if pos - last_pos >= d:
                count += 1
                last_pos = pos
                if count == m:
                    return True
        return False

    low = 1
    high = position[-1] - position[0]
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
```
