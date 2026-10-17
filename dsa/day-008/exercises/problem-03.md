# Problem 3: Longest Duplicate Substring Length

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Multi-variable analysis and binary search with polynomial rolling hash | [Day 8: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given a string `s`, find the maximum length of a substring that occurs at least twice in `s`. The two occurrences may overlap.

Your solution must achieve an expected runtime of $O(N \log N)$ where $N = \text{len}(s)$ and use $O(N)$ auxiliary space.

## Input

`s: str`

## Output

`int`: length of the longest duplicate substring (0 if none exists)

## Constraints

- 2 <= len(s) <= 3 * 10^4
- `s` consists of lowercase English letters only

## Examples

**Example 1**

```text
Input:  s = "banana"
Output: 3
```

"ana" appears twice (starting at index 1 and index 3).

**Example 2**

```text
Input:  s = "abcd"
Output: 0
```

No substring of length >= 1 repeats.

## Function Signature

```python
def longest_duplicate_substring_length(s: str) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Binary search on the candidate length L combined with Rabin-Karp rolling hash to check duplicate existence in O(N) time per length.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
