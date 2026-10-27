# Solution 3: Happy Number

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Cycle detection via a seen-before state set

## Approach

We simulate the process of replacing $n$ with the sum of the squares of its digits. To detect whether the sequence enters an infinite loop, we use a `set` (HashSet) to store all previously seen numbers. If $n$ becomes 1, it is a happy number. If $n$ is encountered in the set, a cycle is detected, and $n$ is not a happy number.

## Thought Process

When repeatedly summing the squares of the digits of a number $n$, the maximum next value for any 32-bit integer (up to $2^{31}-1 \approx 2.14 	imes 10^9$, which has 10 digits) is at most $10 	imes 9^2 = 810$. Thus, numbers quickly shrink into a small bounded range. In this bounded range, the process must either eventually reach 1 or cycle endlessly among a finite set of values. A HashSet allows us to check for previously visited states in $O(1)$ average time, guaranteeing that we detect a cycle or reach 1 in very few steps.

## Algorithm

1. Define a helper function `get_next(num)` that returns the sum of the squares of the digits of `num`.
2. Initialize an empty hash set `seen` to store visited numbers.
3. Loop while `n != 1` and `n not in seen`:
4. Add `n` to `seen`.
5. Update `n = get_next(n)`.
6. Return `True` if `n == 1`, otherwise `False`.

## Complexity Analysis

- **Time:** O(log n) - Each step takes time proportional to the number of digits in $n$, which is $O(\log_{10} n)$. Since $n$ rapidly drops below 243 (for $n \le 2^{31}-1$, the max sum of digit squares is at most $10 \times 81 = 810$), the total number of states visited before hitting 1 or a cycle is bounded by a small constant ($< 1000$).
- **Space:** O(log n) or O(1) bounded space - The hash set `seen` stores a bounded number of unique states (at most a few hundred numbers before cycling or terminating).

## Edge Cases

- n = 1: Already happy, loop terminates immediately and returns True.
- n = 2^31 - 1 (Maximum integer bound): Sum of digit squares calculation completes without overflow or performance issues.
- Cycles not containing 1 (e.g., n = 2, 4): HashSet correctly detects repeating state and returns False.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def get_next(n: int) -> int:
    """Calculate the sum of squares of digits of n."""
    total_sum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total_sum += digit * digit
    return total_sum


def is_happy(n: int) -> bool:
    """Return True if n is a happy number, False otherwise."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
```
