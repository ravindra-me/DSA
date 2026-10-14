# Problem 3: Prime Factor Counting Queries

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Sieve of Eratosthenes with precomputed Smallest Prime Factor (SPF) | [Day 5: Basic Mathematics for DSA](../README.md) |

## Problem Statement

You are given an integer `n` and a list of query integers `queries`. Each query contains a positive integer $x$ ($2 \le x \le n$). For each query, return the count of distinct prime factors of $x$.

Your solution should preprocess integers up to `n` so that each query runs in $O(\text{number of prime factors})$ time.

## Input

`n: int` - upper bound of numbers in queries
`queries: list[int]` - list of integers to analyze where each integer $2 \le x \le n$

## Output

`list[int]` - list of counts of distinct prime factors corresponding to each query

## Constraints

- 2 <= n <= 10^6
- 1 <= len(queries) <= 10^5
- 2 <= queries[i] <= n

## Examples

**Example 1**

```text
Input:  n = 20, queries = [12, 15, 16, 7]
Output: [2, 2, 1, 1]
```

12 = 2^2 * 3 (2 distinct: 2, 3). 15 = 3 * 5 (2 distinct: 3, 5). 16 = 2^4 (1 distinct: 2). 7 is prime (1 distinct: 7).

**Example 2**

```text
Input:  n = 10, queries = [2, 6, 10]
Output: [1, 2, 2]
```

2 has factor [2]; 6 has factors [2, 3]; 10 has factors [2, 5].

## Function Signature

```python
def count_distinct_prime_factors(n: int, queries: list[int]) -> list[int]:
    """Precomputes sieve/SPF up to n and answers distinct prime factor counts for each query."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Precompute the Smallest Prime Factor (SPF) for all numbers up to n using a sieve-like modification. For each query, repeatedly divide by its SPF to extract distinct prime factors in logarithmic time.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
