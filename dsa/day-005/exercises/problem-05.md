# Problem 5: Prime Counting in Ranges (Segmented Sieve)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Segmented Sieve of Eratosthenes | [Day 5: Basic Mathematics for DSA](../README.md) |

## Problem Statement

Given two integers `low` and `high`, return the number of prime numbers in the closed interval `[low, high]`.

While `high` can be as large as $10^9$, the difference `high - low` will not exceed $10^5$. A standard Sieve of Eratosthenes from 1 to `high` will fail due to memory limits, so you must use a Segmented Sieve.

## Input

`low: int`, `high: int` - the range bounds

## Output

`int` - count of prime numbers in `[low, high]`

## Constraints

- 1 <= low <= high <= 10^9
- high - low <= 10^5

## Examples

**Example 1**

```text
Input:  low = 10, high = 20
Output: 4
```

The primes between 10 and 20 are 11, 13, 17, and 19.

**Example 2**

```text
Input:  low = 1, high = 1
Output: 0
```

1 is not prime.

**Example 3**

```text
Input:  low = 1000000000, high = 1000050000
Output: 2441
```

Primes in this 50,000 range near 10^9 are counted using primes up to sqrt(high).

## Function Signature

```python
def count_primes_in_range(low: int, high: int) -> int:
    """Counts primes in [low, high] using a segmented sieve."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Generate base primes up to sqrt(high) with a simple sieve, then mark composites in the segment [low, high] mapped to an array of size (high - low + 1). Target complexity: O(sqrt(high) + (high - low) log log(high)).

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
