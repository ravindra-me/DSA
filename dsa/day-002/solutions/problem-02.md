# Solution 2: Rotate Array by K Steps

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** in-place array reversal and index wrapping

## Approach

Rotating an array right by `k` steps shifts the last `k % n` elements to the front while preserving relative order. We can achieve this in-place with $O(1)$ extra memory using the three-reversal algorithm: reverse the entire array, reverse the first `k % n` elements, and finally reverse the remaining `n - (k % n)` elements.

## Thought Process

A naive approach shifts elements right one-by-one $k$ times, taking $O(k \cdot n)$ time, which is far too slow given $k \le 10^9$ and $n \le 10^5$. Another straightforward approach allocates a new array of size $n$ and places each element at index `(i + k) % n`, taking $O(n)$ time but $O(n)$ extra space, violating the in-place $O(1)$ auxiliary memory requirement.

To achieve both $O(n)$ time and $O(1)$ space, notice the structure of rotation: if $nums = [A, B]$ where $B$ contains the last $k$ elements and $A$ contains the first $n-k$ elements, the desired output is $[B, A]$. Reversing the whole list gives $[B^R, A^R]$. Then, reversing the first $k$ elements turns $B^R$ back into $B$, and reversing the remaining $n-k$ elements turns $A^R$ back into $A$, yielding $[B, A]$. First taking $k = k \pmod n$ ensures we handle cases where $k \ge n$ without redundant work.

## Algorithm

1. Normalize `k` by taking `k = k % len(nums)`. If `k == 0` or `len(nums) <= 1`, return immediately as no elements need to move.
2. Define an in-place two-pointer helper function `reverse(start, end)` that swaps elements from `start` to `end` inward until pointers meet.
3. Reverse the entire array: `reverse(0, len(nums) - 1)`.
4. Reverse the first `k` elements: `reverse(0, k - 1)`.
5. Reverse the remaining `n - k` elements: `reverse(k, len(nums) - 1)`.

## Complexity Analysis

- **Time:** O(n) because reversing a subarray of length m takes m // 2 swaps; the three reversals visit each element at most twice overall.
- **Space:** O(1) auxiliary memory since all reversals are performed strictly in-place using two pointer indices.

## Edge Cases

- k == 0 or k is a multiple of len(nums): k % len(nums) becomes 0, and the array remains unchanged.
- k > len(nums): k % len(nums) wraps correctly to an effective shift between 0 and len(nums) - 1.
- Single-element array (len(nums) == 1): normalized k is always 0, no modifications occur.
- Negative numbers and duplicates: reversal purely manipulates indices regardless of element values.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def rotate(nums: list[int], k: int) -> None:
    """Rotate nums to the right by k steps in-place."""
    n = len(nums)
    if n <= 1:
        return
    
    k %= n
    if k == 0:
        return

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
```
