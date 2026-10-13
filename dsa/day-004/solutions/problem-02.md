# Solution 2: Power Function

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Divide and conquer (Exponentiation)

## Approach

We use Exponentiation by Squaring (also known as binary exponentiation) to solve this problem. Instead of multiplying the base `N` times, which is O(N), we recursively halve the exponent. If the current exponent is even, `base^exp` is `(base^2)^(exp/2)`. If it is odd, `base^exp` is `base * (base^2)^((exp-1)/2)`. This reduces the problem size by half at every recursive step.

## Thought Process

A naive approach would simply loop `exp` times multiplying the base, resulting in O(N) time complexity. However, we notice that `x^10` is equivalent to `(x^2)^5`. We can calculate `x^2` once, and then raise that to the power of 5. By observing these patterns (halving the exponent), we can arrive at an O(log N) recursive solution. We must handle the base case (exp == 0) and the odd exponent case explicitly.

## Algorithm

1. 1. Define a base case: if exp is 0, return 1.
2. 2. If exp is even, return power(base * base, exp // 2).
3. 3. If exp is odd, return base * power(base * base, (exp - 1) // 2).

## Complexity Analysis

- **Time:** O(log N), where N is the exponent, because the exponent is halved in each recursive step.
- **Space:** O(log N) due to the recursive call stack depth.

## Edge Cases

- exp = 0: Correctly returns 1 immediately.
- base = 0: Returns 0 (unless exp=0, which returns 1).
- base = 1: Returns 1 for any non-negative exp.
- base = -1: Correctly handles sign flipping based on odd/even exponent.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def power(base: int, exp: int) -> int:
    """Calculates base^exp efficiently using binary exponentiation."""
    if exp == 0:
        return 1
    
    # Divide and conquer approach:
    # If even: (base^2)^(exp/2)
    # If odd: base * (base^2)^((exp-1)/2)
    if exp % 2 == 0:
        return power(base * base, exp // 2)
    else:
        return base * power(base * base, exp // 2)
```
