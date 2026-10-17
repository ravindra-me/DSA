# Problem 2: Continuous Resettable Counter

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Amortized state updates with lazy propagation | [Day 8: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Design a data structure that maintains an array of $n$ counters (all initially 0, indexed $0$ to $n - 1$) supporting three operations:
- `increment(i)`: adds 1 to counter $i$.
- `set_all(val)`: sets all $n$ counters to `val`.
- `get(i)`: returns the current value of counter $i$.

Each operation must run in $O(1)$ worst-case time (not $O(n)$ for `set_all`). The total space must be $O(n)$.

## Input

Operations on class `ResettableCounters` initialized with `size: int`

## Output

Integer values for `get(i)` queries

## Constraints

- 1 <= size <= 10^5
- Total number of operations <= 2 * 10^5
- 0 <= val <= 10^9
- 0 <= i < size

## Examples

**Example 1**

```text
Input:  rc = ResettableCounters(3)
rc.increment(0)
rc.set_all(5)
rc.increment(1)
[rc.get(0), rc.get(1), rc.get(2)]
Output: [5, 6, 5]
```

rc[0] is set to 5 by set_all. rc[1] becomes 5 then incremented to 6. rc[2] receives the baseline 5.

**Example 2**

```text
Input:  rc = ResettableCounters(1)
rc.get(0)
Output: 0
```

Initial values default to 0.

## Function Signature

```python
class ResettableCounters:
    def __init__(self, size: int) -> None:
        pass

    def increment(self, i: int) -> None:
        pass

    def set_all(self, val: int) -> None:
        pass

    def get(self, i: int) -> int:
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a baseline value and a timestamp/generation tracking system per index to avoid updating all N elements during set_all.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
