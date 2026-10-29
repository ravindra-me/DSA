# Problem 4: Prime Digit Circular Shifts

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Sieve of Eratosthenes & Digit Manipulation | [Day 20: Basic Mathematics for DSA](../README.md) |

## Problem Statement

A number is called a **Circular Prime** if all cyclic rotations of its decimal digits are themselves prime (e.g., 197 is a circular prime because 197, 971, and 719 are all prime).

Given an integer `limit`, find the count of circular primes strictly less than `limit`.

Note: Single-digit primes (2, 3, 5, 7) are trivially circular primes.

## Input

An integer `limit: int`.

## Output

An integer representing the count of circular primes strictly less than `limit`.

## Constraints

- 2 <= limit <= 1000000

## Examples

**Example 1**

```text
Input:  limit = 100
Output: 13
```

The 13 circular primes below 100 are: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

**Example 2**

```text
Input:  limit = 2
Output: 0
```

There are no primes strictly less than 2.

## Function Signature

```python
def count_circular_primes(limit: int) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use the Sieve of Eratosthenes to precompute primes up to limit. For each prime, generate its digit rotations and verify primality using the sieve in O(limit log log limit).

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
