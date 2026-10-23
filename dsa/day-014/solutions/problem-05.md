# Solution 5: Shortest Palindrome via Prefix Prepending

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Finding the longest palindromic prefix using rolling hash or prefix-suffix matching

## Approach

We need to find the longest palindromic prefix of `s`. By taking the characters after this prefix, reversing them, and prepending them to `s`, we get the shortest possible palindrome. We can find the longest palindromic prefix in linear time using the KMP prefix function (or rolling hash) on the combined string `s + '#' + reversed(s)`.

## Thought Process

Prepending characters to `s` means that the suffix of the prepended portion and the prefix of `s` must mirror each other. Since we want to prepend the fewest characters, we want to maximize the length of the prefix of `s` that is already a palindrome. Any remaining characters after this longest palindromic prefix must be reversed and attached in front.

A brute-force approach checks every prefix of `s` starting from length `n` down to 1 to see if it is a palindrome. In the worst case (e.g., `s = "a" * 25000 + "b"`), checking takes $O(n^2)$ time, which times out for $n = 5 \times 10^4$.

To optimize, observe that a prefix of `s` of length $L$ is a palindrome if and only if it equals the suffix of length $L$ of $s^{rev}$ (the reversed string). Thus, we want to find the longest prefix of `s` that is also a suffix of $s^{rev}$. This is precisely what the Knuth-Morris-Pratt (KMP) failure table (prefix function $\pi$) computes! If we construct a combined string $T = s + \text{'#'} + s^{rev}$ (where `'#'` is a delimiter not present in $s$), the last entry of the KMP $\pi$ table for $T$ gives the length of the longest proper prefix of $T$ that matches a suffix of $T$. Because the delimiter prevents matches longer than $|s|$, this length is exactly the length of the longest palindromic prefix of $s$.

## Algorithm

1. Handle the trivial case: if `s` is empty or has length 1, return `s`.
2. Form the combined string `combined = s + '#' + s[::-1]`.
3. Compute the KMP prefix function (pi table) for `combined`, where `pi[i]` denotes the length of the longest proper prefix of `combined[0..i]` that is also a suffix of `combined[0..i]`.
4. Initialize `pi = [0] * len(combined)`. Use two pointers `j = 0` and iterate `i` from 1 to `len(combined) - 1`.
5. While `j > 0` and `combined[i] != combined[j]`, backtrack with `j = pi[j - 1]`.
6. If `combined[i] == combined[j]`, increment `j` by 1, and set `pi[i] = j`.
7. The length of the longest palindromic prefix of `s` is `L = pi[-1]`.
8. The remaining suffix of `s` that is not part of the palindrome is `s[L:]`. Reverse this suffix and prepend it to `s`: return `s[L:][::-1] + s`.

## Complexity Analysis

- **Time:** O(n) where n is the length of `s`. Computing the reversed string takes O(n), and computing the KMP prefix table for a string of length 2n + 1 takes O(n) steps because the inner while loop amortizes to O(n).
- **Space:** O(n) to store the reversed string, the combined string, and the KMP prefix array of size 2n + 1.

## Edge Cases

- Empty string (`""`): handled immediately, returns `""`.
- Single character (`"a"`): already a palindrome, returns `"a"`.
- String is already a palindrome (e.g., `"racecar"`): prefix function gives `len(s)`, prepends nothing, returns `s`.
- No repeating characters or palindrome prefix > 1 (e.g., `"abcd"`): prepends reversed suffix `"dcb"`, returns `"dcbabcd"`.
- All identical characters (e.g., `"aaaa"`): correctly identifies the whole string as palindromic and returns `s`.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def shortest_palindrome(s: str) -> str:
    """Find the shortest palindrome by prepending characters to s."""
    if len(s) <= 1:
        return s

    # Combine s, a delimiter, and reversed s
    # The delimiter '#' ensures prefix matches cannot span across the two parts.
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    n = len(combined)

    # Compute KMP prefix table (pi array)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and combined[i] != combined[j]:
            j = pi[j - 1]
        if combined[i] == combined[j]:
            j += 1
        pi[i] = j

    # pi[-1] is the length of the longest palindromic prefix of s
    longest_pal_prefix_len = pi[-1]
    non_pal_suffix = s[longest_pal_prefix_len:]
    return non_pal_suffix[::-1] + s
```
