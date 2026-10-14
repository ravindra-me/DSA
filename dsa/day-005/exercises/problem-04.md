# Problem 4: Modular Exponentiation Matrix Series

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Fast binary exponentiation and modular arithmetic properties | [Day 5: Basic Mathematics for DSA](../README.md) |

## Problem Statement

Given three integers `a`, `b`, and `m`, compute the sum of the geometric progression modulo `m`:

$$S = \sum_{i=0}^{k} a^i \pmod m = (a^0 + a^1 + a^2 + \dots + a^k) \pmod m$$

Because $k$ can be as large as $10^9$, an $O(k)$ linear loop will exceed the time limit. Notice that $m$ is not guaranteed to be prime, so standard modular division using Fermat's Little Theorem cannot be applied directly.

## Input

`a: int`, `k: int`, `m: int` where $a \ge 0$, $k \ge 0$, and $m \ge 2$

## Output

`int` - the value of $(a^0 + a^1 + \dots + a^k) \pmod m$

## Constraints

- 0 <= a <= 10^9
- 0 <= k <= 10^9
- 2 <= m <= 10^9 + 7

## Examples

**Example 1**

```text
Input:  a = 2, k = 3, m = 1000
Output: 15
```

2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15. 15 % 1000 = 15.

**Example 2**

```text
Input:  a = 3, k = 0, m = 7
Output: 1
```

3^0 = 1. 1 % 7 = 1.

**Example 3**

```text
Input:  a = 5, k = 4, m = 6
Output: 5
```

5^0 + 5^1 + 5^2 + 5^3 + 5^4 = 1 + 5 + 25 + 125 + 625 = 781. 781 % 6 = 5.

## Function Signature

```python
def geometric_sum_mod(a: int, k: int, m: int) -> int:
    """Computes (sum_{i=0}^k a^i) % m in O(log k) time."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use divide-and-conquer recursion or binary exponentiation on a 2x2 matrix representation in O(log k) time without needing division.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
