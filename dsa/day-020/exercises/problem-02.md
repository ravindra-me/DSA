# Problem 2: Kth Digit of a Geometric Product

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Fast Modular Exponentiation and Logarithmic Math | [Day 20: Basic Mathematics for DSA](../README.md) |

## Problem Statement

Consider a geometric sequence starting at `a` with common ratio `r` of length `n`, i.e., terms are $a, a \cdot r, a \cdot r^2, \dots, a \cdot r^{n-1}$.

The product of all $n$ terms is $P = a^n \cdot r^{\frac{n(n-1)}{2}}$.

Given integers `a`, `r`, and `n`, return the last $k$ digits of $P$ as an integer (i.e. $P \pmod{10^k}$).

## Input

Three integers `a`, `r`, `n` and an integer `k` specifying the number of trailing digits.

## Output

An integer representing $P \pmod{10^k}$.

## Constraints

- 1 <= a, r <= 10^9
- 1 <= n <= 10^9
- 1 <= k <= 9

## Examples

**Example 1**

```text
Input:  a = 2, r = 3, n = 3, k = 4
Output: 216
```

Terms are [2, 6, 18]. Product is 2 * 6 * 18 = 216. 216 % 10000 = 216.

**Example 2**

```text
Input:  a = 10, r = 10, n = 1, k = 2
Output: 10
```

Single term 10. 10 % 100 = 10.

## Function Signature

```python
def kth_digit_geometric_product(a: int, r: int, n: int, k: int) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Simplify the total exponent of r, then compute modular exponentiation of a^n and r^(n*(n-1)//2) modulo 10^k in O(log n) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
