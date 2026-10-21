# Solution 5: Sum of Subarray Minimums

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Counting subarrays where each element is the minimum using PSE and NSE

## Approach

Instead of generating every subarray and finding its minimum, determine for each element `arr[i]` how many subarrays have `arr[i]` as their minimum. Using a monotonic increasing stack, find the distance to the Previous Less Element (PLE) and Next Less or Equal Element (NLEE) for each index. The total contribution of `arr[i]` is `arr[i] * (i - ple) * (nlee - i)`. Summing these contributions modulo $10^9 + 7$ yields the result in linear time.

## Thought Process

A brute-force approach iterates over all $O(n^2)$ contiguous subarrays and finds the minimum in each, taking $O(n^2)$ time with incremental updates or $O(n^3)$ naively. For $n = 10^5$, an $O(n^2)$ algorithm is far too slow.

We invert the problem: instead of asking 'for each subarray, what is its minimum?', we ask 'for each element `arr[i]`, in how many subarrays is it the minimum?'

A subarray $[L, R]$ has `arr[i]` as its minimum if $L \le i \le R$ and all elements in `arr[L..R]` are $\ge arr[i]$. Thus, $L$ can extend leftwards until we hit an element smaller than `arr[i]`, and $R$ can extend rightwards until we hit an element smaller than `arr[i]`.

To handle duplicates correctly without double-counting subarrays that share the same minimum value, we define an asymmetry: look strictly for elements `< arr[i]` to the left (Previous Less Element), but `<= arr[i]` to the right (Next Less or Equal Element). This ensures each subarray's minimum is uniquely attributed to the first occurrence (or last occurrence, depending on convention) of that minimum value.

Both PLE and NLEE can be computed in a single pass (or two passes) using a monotonic stack in $O(n)$ time.

## Algorithm

1. Initialize `MOD = 1_000_000_007`, `n = len(arr)`, and arrays `ple` and `nle` of length `n`.
2. Initialize `ple[i] = -1` for all `i`, representing no smaller element to the left.
3. Initialize `nle[i] = n` for all `i`, representing no smaller or equal element to the right.
4. Iterate `i` from `0` to `n - 1` using a monotonic increasing stack to find `ple`: pop elements from the stack while `arr[stack[-1]] >= arr[i]`. If the stack is not empty, `ple[i] = stack[-1]`. Push `i` onto the stack.
5. Clear the stack. Iterate `i` from `n - 1` down to `0` using a monotonic stack to find `nle`: pop elements from the stack while `arr[stack[-1]] > arr[i]`. If the stack is not empty, `nle[i] = stack[-1]`. Push `i` onto the stack.
6. Compute total sum: for each `i`, add `arr[i] * (i - ple[i]) * (nle[i] - i)` to `total`, maintaining `total % MOD`.
7. Return `total % MOD`.

## Complexity Analysis

- **Time:** O(n) where n is the length of `arr`. Each index is pushed and popped from the stack at most once in each pass.
- **Space:** O(n) to store the monotonic stack and the boundary arrays `ple` and `nle`.

## Edge Cases

- Single element (`len(arr) == 1`): directly yields `arr[0] % MOD` as `ple = -1` and `nle = 1` giving count 1.
- All identical elements: asymmetry (`>=` for left vs `>` for right) ensures each subarray with duplicates is counted exactly once without overlap or omission.
- Strictly increasing array: each element's left range is 1, right range extends to the end of the array.
- Strictly decreasing array: each element's left range extends to index 0, right range is 1.
- Large values and sum exceeding 32-bit integer: modulo arithmetic is applied at each step and returned properly.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def sum_subarray_mins(arr: list[int]) -> int:
    """Compute sum of all contiguous subarray minimums modulo 10^9 + 7."""
    MOD = 1_000_000_007
    n = len(arr)
    if n == 0:
        return 0

    # ple[i] stores the index of the previous strictly less element
    ple = [-1] * n
    # nle[i] stores the index of the next less or equal element
    nle = [n] * n

    # Compute PLE
    stack: list[int] = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            ple[i] = stack[-1]
        stack.append(i)

    # Compute NLE
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            nle[i] = stack[-1]
        stack.append(i)

    total = 0
    for i in range(n):
        left_count = i - ple[i]
        right_count = nle[i] - i
        total = (total + arr[i] * left_count * right_count) % MOD

    return total
```
