# Solution 4: Find Longest Awesome Substring

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Prefix parity bitmask combined with hash map for palindrome eligibility

## Approach

A string can be rearranged into a palindrome if and only if at most one digit appears an odd number of times. We can represent the parity (even/odd) of counts for digits 0-9 using a 10-bit integer (bitmask). By maintaining a running prefix bitmask as we traverse the string, the parity of digit counts in substring `s[j:i]` is given by `prefix_mask[i] ^ prefix_mask[j]`. A valid awesome substring requires this XOR sum to be `0` (all even counts) or `1 << d` for some digit `d` (exactly one odd count). We can store the earliest index where each mask was seen in a map/array to maximize substring lengths in $O(1)$ time per character.

## Thought Process

Checking all $O(N^2)$ substrings directly and verifying palindrome eligibility takes $O(N^3)$ or $O(N^2)$ time, which will time out given $N \le 10^5$. 

Since we only care about parity of counts for 10 distinct digits ('0'-'9'), the search space of state parities is extremely small: $2^{10} = 1024$ possible bitmasks. 

If we compute prefix bitmasks `mask` where bit $d$ is flipped whenever digit $d$ is seen, the bitmask for substring $s[j:i]$ is `mask[i] ^ mask[j]`. 
- For all counts to be even: `mask[i] ^ mask[j] == 0` $\implies$ `mask[j] == mask[i]`. 
- For exactly one count to be odd: `mask[i] ^ mask[j] == (1 << d)` $\implies$ `mask[j] == mask[i] ^ (1 << d)` for some $d \in [0, 9]$.

By storing the first occurrence index of every seen bitmask in a fixed-size array of length 1024 (initialized to $\infty$), we can check all 11 possible matching prefix masks in $O(1)$ time at each index $i$, achieving optimal $O(N)$ time complexity.

## Algorithm

1. Initialize an array `seen` of size 1024 with value infinity, and set `seen[0] = -1` (representing an empty prefix before index 0).
2. Initialize `mask = 0`, `max_len = 0`.
3. Iterate through index `i` and character `ch` in `s`:
4. Compute `digit = int(ch)` and flip bit `digit` in `mask`: `mask ^= (1 << digit)`.
5. If `seen[mask]` has been recorded, update `max_len = max(max_len, i - seen[mask])`.
6. For each digit `d` from 0 to 9, check `target = mask ^ (1 << d)`. If `seen[target]` has been recorded, update `max_len = max(max_len, i - seen[target])`.
7. If `seen[mask]` is still infinity, set `seen[mask] = i` (record first occurrence).
8. Return `max_len`.

## Complexity Analysis

- **Time:** $O(N \cdot |\Sigma|) = O(10N) = O(N)$, where $N$ is the length of string `s` and $|\Sigma| = 10$ is the alphabet size.
- **Space:** $O(2^{|\Sigma|}) = O(1024) = O(1)$ space to store the earliest index array for all possible bitmasks.

## Edge Cases

- Single-character strings: Handles correctly because any single digit can be rearranged into a palindrome of length 1.
- All identical characters: All parity states repeatedly switch between 0 and 1; the full length is captured.
- No multi-character palindrome possible (e.g. "12345678"): Length 1 will be found for every single character.
- Entire string is awesome: Initializing `seen[0] = -1` allows substrings starting at index 0 to be correctly evaluated.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def longest_awesome(s: str) -> int:
    """Find length of longest substring that can be rearranged into a palindrome."""
    seen = [-2] * 1024
    seen[0] = -1
    
    mask = 0
    max_len = 0
    
    for i, ch in enumerate(s):
        digit = ord(ch) - ord('0')
        mask ^= (1 << digit)
        
        # Case 1: All digits in substring have even count
        if seen[mask] != -2:
            max_len = max(max_len, i - seen[mask])
        
        # Case 2: Exactly one digit in substring has odd count
        for d in range(10):
            target_mask = mask ^ (1 << d)
            if seen[target_mask] != -2:
                max_len = max(max_len, i - seen[target_mask])
        
        # Record first time seeing this mask
        if seen[mask] == -2:
            seen[mask] = i
            
    return max_len
```
