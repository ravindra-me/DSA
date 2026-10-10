# Solution 5: First Missing Positive

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** In-place cyclic indexing to achieve O(n) time and O(1) auxiliary space

## Approach

Use the array itself as a hash table via cyclic sorting (in-place index mapping). For an array of length $n$, the smallest missing positive integer must fall in the range $[1, n + 1]$. We iterate through the array and place each valid number $x \in [1, n]$ at its matching index $x - 1$ by swapping. After placing all possible elements in their correct spots, the first index $i$ where `nums[i] != i + 1` indicates that $i + 1$ is the first missing positive.

## Thought Process

### 1. Brute Force & Space Trade-offs
- **Brute Force**: Check $k = 1, 2, 3, \dots$ by performing a linear scan in `nums` for each $k$. In the worst case, this requires $O(n^2)$ time and $O(1)$ space.
- **Hash Set**: Insert all elements into a hash set and query $1, 2, \dots, n + 1$. This takes $O(n)$ time, but $O(n)$ auxiliary space, which violates the strict $O(1)$ space constraint.
- **Sorting**: Sort the array in $O(n \log n)$ time and then scan linearly. This takes $O(1)$ auxiliary space (with in-place heapsort), but exceeds $O(n)$ time.

### 2. Pigeonhole Principle & The Key Insight
If an array has length $n$, the best-case sequence of positive integers is $[1, 2, \dots, n]$. If all of these numbers are present, the answer is $n + 1$. If even a single number in $[1, n]$ is missing, the answer must be between $1$ and $n$ inclusive. Therefore, the answer is guaranteed to be in the range $[1, n + 1]$.

Any number $\le 0$ or $> n$ is irrelevant to the answer. We only care about positive integers $x \in [1, n]$.

### 3. In-Place Cyclic Indexing
Since we need $O(1)$ auxiliary space, we can repurpose `nums` as our hash set. Specifically, the number $x$ should ideally live at index $x - 1$.
We can iterate through the array: while the current number `nums[i]` is in the range $[1, n]$ and not already at its correct destination `nums[nums[i] - 1]`, we swap `nums[i]` with the value at `nums[i] - 1`.

Each swap places at least one number into its final correct position, so the total number of swaps across the entire pass is bounded by $n$. Thus, the placement loop runs in $O(n)$ total time.

## Algorithm

1. Determine $n = \text{len}(nums)$.
2. Iterate through index $i$ from $0$ to $n - 1$.
3. While $1 \le nums[i] \le n$ and $nums[i] \ne nums[nums[i] - 1]$, swap $nums[i]$ with $nums[nums[i] - 1]$. If $nums[i] == nums[nums[i] - 1]$, break the while loop to avoid infinite loops caused by duplicates.
4. After the cyclic placement completes, make a second pass through the array from $i = 0$ to $n - 1$.
5. Return $i + 1$ for the first index where $nums[i] \ne i + 1$.
6. If all positions $0$ through $n - 1$ satisfy $nums[i] == i + 1$, all numbers from $1$ to $n$ are present; return $n + 1$.

## Complexity Analysis

- **Time:** $O(n)$ total time. Although there is a nested `while` loop, each swap places at least one number $x$ into its correct location `nums[x - 1]`. Since an element never moves again once placed correctly, at most $n$ swaps occur across the entire algorithm. The subsequent verification loop takes $O(n)$ time.
- **Space:** $O(1)$ auxiliary space. The swaps are performed in-place within the input array using only a constant number of scalar index variables.

## Edge Cases

- Single element array `[1]`: Returns `2`; array `[2]` or `[-5]` returns `1`.
- All non-positive numbers (e.g. `[-1, -2, 0]`): None are in $[1, n]$, no swaps occur, returns `1`.
- Duplicate positive numbers (e.g. `[1, 1]` or `[2, 2]`): The condition `nums[i] != nums[correct_idx]` prevents an infinite swap cycle.
- Array is an exact contiguous permutation `[1, 2, ..., n]`: Every element matches its index; returns `n + 1`.
- Extremely large integers out of 32-bit range: Filtered out by the range check $1 \le nums[i] \le n$.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def first_missing_positive(nums: list[int]) -> int:
    """Return the smallest positive integer missing from nums.

    Runs in O(n) time and O(1) auxiliary space via in-place cyclic indexing.
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
```
