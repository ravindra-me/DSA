# Solution 2: Pairwise Array Reduction

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Euclidean GCD and LCM across multiple values

## Approach

Both GCD and LCM are associative and commutative binary operations. We can compute the overall GCD and LCM by reducing the array from left to right: accumulate the current GCD using the Euclidean algorithm, and accumulate the current LCM using the identity $\text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$.

## Thought Process

A naive approach might attempt to find prime factorizations of all numbers or iterate through multiples/divisors. However, factoring numbers up to $10^6$ for $10^4$ elements is unnecessary and slow. Instead, we use the properties of GCD and LCM: $\gcd(a, b, c) = \gcd(\gcd(a, b), c)$ and $\text{lcm}(a, b, c) = \text{lcm}(\text{lcm}(a, b), c)$. For two numbers, Euclidean algorithm finds $\gcd(a, b)$ in logarithmic time $O(\log(\min(a, b)))$. Then, $\text{lcm}(a, b) = (a // \gcd(a, b)) * b$, avoiding unnecessary intermediate overflow by dividing before multiplying. Python handles arbitrarily large integers automatically, so accumulating LCM across the array will not overflow standard integer limits.

## Algorithm

1. Initialize `current_gcd` and `current_lcm` with `nums[0]`.
2. Define a helper or use `math.gcd` to compute greatest common divisor.
3. For each subsequent number `x` in `nums[1:]`:
4. Update `current_gcd = math.gcd(current_gcd, x)`.
5. Update `current_lcm = (current_lcm // math.gcd(current_lcm, x)) * x`.
6. Early exit optimization: if `current_gcd == 1`, further GCD operations will remain 1, though LCM still needs to be computed.
7. Return `(current_gcd, current_lcm)`.

## Complexity Analysis

- **Time:** O(N * log(M)) where N is the length of `nums` and M is the maximum value in `nums`. Each pair-wise GCD evaluation takes logarithmic time with respect to the numbers.
- **Space:** O(1) auxiliary space beyond holding the accumulating LCM integer.

## Edge Cases

- Single element array: Returns `(nums[0], nums[0])` directly.
- All identical elements: GCD and LCM will both equal the repeated element.
- Coprime elements: GCD drops to 1 quickly.
- Array with element 1: GCD becomes 1, LCM is unaffected by 1.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
import math
from typing import Sequence

def array_gcd_lcm(nums: Sequence[int]) -> tuple[int, int]:
    """Computes the overall GCD and LCM of an array of positive integers."""
    if not nums:
        raise ValueError("nums must not be empty")

    current_gcd = nums[0]
    current_lcm = nums[0]

    for x in nums[1:]:
        if current_gcd != 1:
            current_gcd = math.gcd(current_gcd, x)
        
        # lcm(a, b) = (a * b) // gcd(a, b)
        # Dividing first keeps intermediate numbers smaller
        current_lcm = (current_lcm // math.gcd(current_lcm, x)) * x

    return current_gcd, current_lcm
```
