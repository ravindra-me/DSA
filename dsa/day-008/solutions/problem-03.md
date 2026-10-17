# Solution 3: Longest Duplicate Substring Length

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Multi-variable analysis and binary search with polynomial rolling hash

## Approach

We binary search on the length $L$ of the duplicate substring in the range $[1, N - 1]$. For a fixed candidate length $L$, we check for duplicate substrings in $O(N)$ time using the Rabin-Karp polynomial rolling hash technique with a double hash (or a 61-bit Mersenne prime) to avoid collisions.

## Thought Process

A naive brute-force approach checks every possible substring of length $L$ for every $L \in [1, N - 1]$. There are $O(N^2)$ substrings in total, and comparing strings naively takes $O(N)$, resulting in an $O(N^3)$ algorithm. Even using a hash set of sliced strings would take $O(N^2)$ time and memory because slicing creates string copies.

To optimize, we observe a monotonic property: if there exists a duplicate substring of length $L$, any prefix of that duplicate is a duplicate substring of length $L' < L$. Conversely, if no duplicate substring of length $L$ exists, no duplicate of length $> L$ can exist. This monotonicity permits binary searching on $L \in [1, N - 1]$, requiring $O(\log N)$ validation steps.

For a fixed $L$, we can slide a window of length $L$ across the string. Instead of slicing, we compute the polynomial rolling hash of the window in $O(1)$ amortized time per step. To virtually eliminate hash collisions without storing substring slices, we can use a double hash with two large distinct prime moduli (e.g., $10^9 + 7$ and $10^9 + 9$) and base 26 (or larger). If a hash pair has been seen before, a duplicate substring of length $L$ exists.

## Algorithm

1. Binary search on the duplicate length $L$ with search space `low = 1` and `high = len(s) - 1`.
2. Define a predicate `has_duplicate(L)` that returns `True` if any substring of length $L$ appears at least twice.
3. Inside `has_duplicate(L)`, compute the initial hash of `s[0:L]` for two primes $M_1 = 10^9 + 7$ and $M_2 = 10^9 + 9$ with base $B = 31$. Precompute $B^L \pmod{M_1}$ and $B^L \pmod{M_2}$.
4. Store seen hash pairs `(hash1, hash2)` in a hash set.
5. Slide the window across $s$ from index $1$ to $N - L$: update each hash in $O(1)$ by subtracting the outgoing character contribution and adding the incoming character.
6. If the new `(hash1, hash2)` is already in the set, return `True`. Otherwise, add it.
7. If `has_duplicate(mid)` is true, record `mid` as a valid answer and search higher (`low = mid + 1`); otherwise search lower (`high = mid - 1`).
8. Return the maximum valid $L$ found (or 0 if none).

## Complexity Analysis

- **Time:** $O(N \log N)$ expected: The binary search takes $O(\log N)$ iterations. In each iteration, `has_duplicate(L)` slides an $O(1)$ hash calculation across $N - L + 1$ windows, which takes $O(N)$ time. Double hashing makes hash collisions negligible.
- **Space:** $O(N)$ auxiliary space to store up to $N - L + 1$ integer hash pairs in the hash set during each check.

## Edge Cases

- No duplicates exist (e.g. "abcd"): binary search never finds a valid length and returns 0.
- Overlapping duplicates (e.g. "banana" with "ana" or "aaaa" with "aaa"): rolling hash detects duplicates regardless of whether index ranges overlap.
- Minimum length string $N = 2$ with no duplicate (e.g. "ab") or duplicate ("aa"): handles boundaries correctly.
- String of identical characters (e.g. "aaaaa"): maximum duplicate length is $N - 1$.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def longest_duplicate_substring_length(s: str) -> int:
    """Return the maximum length of a duplicate substring in s."""
    n = len(s)
    if n <= 1:
        return 0

    nums = [ord(c) - ord("a") for c in s]
    base = 31
    mod1 = 1_000_000_007
    mod2 = 1_000_000_009

    def has_duplicate(length: int) -> bool:
        h1, h2 = 0, 0
        power1, power2 = 1, 1
        for i in range(length):
            h1 = (h1 * base + nums[i]) % mod1
            h2 = (h2 * base + nums[i]) % mod2
            if i < length - 1:
                power1 = (power1 * base) % mod1
                power2 = (power2 * base) % mod2

        seen = {(h1, h2)}
        for i in range(length, n):
            h1 = (h1 - nums[i - length] * power1) % mod1
            h1 = (h1 * base + nums[i]) % mod1

            h2 = (h2 - nums[i - length] * power2) % mod2
            h2 = (h2 * base + nums[i]) % mod2

            pair = (h1, h2)
            if pair in seen:
                return True
            seen.add(pair)

        return False

    low, high = 1, n - 1
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if has_duplicate(mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best
```
