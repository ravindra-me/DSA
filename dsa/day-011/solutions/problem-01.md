# Solution 1: Sort Array by Parity II

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** two-pointers-invariants

## Approach

Maintain two pointers: one stepping through even indices (`even_idx = 0`) and one stepping through odd indices (`odd_idx = 1`). Advance each pointer until an element violates the expected parity at that index, then swap the two misplaced elements and continue.

## Thought Process

A naive or brute-force approach might collect all even numbers in one list and all odd numbers in another, then interleave them back into the array. While this takes $O(N)$ time, it requires $O(N)$ auxiliary space.

To achieve $O(1)$ auxiliary space in-place, observe the invariant: every misplaced even index must contain an odd number, and because the array has an equal number of even and odd integers, every misplaced odd index must contain an even number. 

Therefore, a misplaced odd number at an even index always has a corresponding misplaced even number at an odd index. By advancing `even_idx` by $+2$ until finding an odd number, advancing `odd_idx` by $+2$ until finding an even number, and swapping their values, both indices are fixed simultaneously. Repeating this until either pointer goes out of bounds guarantees all elements satisfy the parity condition.

## Algorithm

1. Initialize pointer `even_idx = 0` and pointer `odd_idx = 1`.
2. While `even_idx < len(nums)` and `odd_idx < len(nums)`:
3. Advance `even_idx` by 2 as long as `even_idx < len(nums)` and `nums[even_idx] % 2 == 0`.
4. Advance `odd_idx` by 2 as long as `odd_idx < len(nums)` and `nums[odd_idx] % 2 == 1`.
5. If both pointers are still within bounds, swap `nums[even_idx]` and `nums[odd_idx]`.
6. Return the mutated `nums` list.

## Complexity Analysis

- **Time:** $O(N)$ because each index in the array is examined at most once by either `even_idx` or `odd_idx`.
- **Space:** $O(1)$ auxiliary space because elements are swapped directly in-place with only index pointers.

## Edge Cases

- Smallest valid length (len = 2): handled directly with at most one swap.
- Array already satisfied: pointers traverse to the end without any swaps.
- Array completely inverted (all even values at odd indices and vice versa): swaps occur at every pair.
- Duplicate values and zero: zero is treated as even (`0 % 2 == 0`), duplicate values swap correctly according to parity.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    """Sorts array in-place such that even indices have even values and odd indices have odd values."""
    n = len(nums)
    even_idx = 0
    odd_idx = 1

    while even_idx < n and odd_idx < n:
        while even_idx < n and nums[even_idx] % 2 == 0:
            even_idx += 2
        while odd_idx < n and nums[odd_idx] % 2 == 1:
            odd_idx += 2
        
        if even_idx < n and odd_idx < n:
            nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            even_idx += 2
            odd_idx += 2

    return nums
```
