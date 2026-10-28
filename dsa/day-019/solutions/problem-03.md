# Solution 3: Group Anagrams by Count Signature

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** canonical frequency signatures as dictionary keys

## Approach

Represent each string's character distribution as a fixed-length 26-tuple of character frequencies. Use this hashable tuple as a dictionary key to group words, preserving their encounter order, and finally sort the groups primarily by length descending and secondarily by the first word lexicographically.

## Thought Process

A brute-force comparison between every pair of strings takes $O(N^2 \cdot L)$ time, where $N$ is the number of strings and $L$ is the maximum string length. Alternatively, sorting each string to obtain a canonical key takes $O(N \cdot L \log L)$. Since the character set is restricted to lowercase English letters ('a'-'z'), we can generate a canonical signature in linear $O(L)$ time per string by counting character frequencies into a 26-element array and converting it into an immutable tuple. Using a hash table keyed on these tuples clusters anagrams in $O(N \cdot L)$ time. Finally, the problem requires a specific order: groups sorted by size descending, ties broken lexicographically by the group's first element, which can be accomplished with a standard sort key `(-len(group), group[0])`.

## Algorithm

1. Initialize a `collections.defaultdict(list)` named `groups` mapping signature tuples to lists of strings.
2. For each word `s` in `strs`, construct an array of size 26 initialized to 0.
3. For each character `ch` in `s`, increment `count[ord(ch) - ord('a')]`.
4. Convert the count array to a tuple and append `s` to `groups[tuple(count)]` to maintain encounter order within each group.
5. Extract all group lists from `groups.values()`.
6. Sort the list of groups using the key `lambda group: (-len(group), group[0])`.
7. Return the sorted list of groups.

## Complexity Analysis

- **Time:** O(N * L + K log K) where N is the number of strings, L is the maximum length of a string (up to 100), and K <= N is the number of distinct anagram groups. Counting frequencies takes O(N * L), and sorting the K groups takes O(K log K * L). Given constraints, this runs in a few milliseconds.
- **Space:** O(N * L) auxiliary space to store the hash map and resulting groups.

## Edge Cases

- Empty strings: Count array is all zeros (26 zeros), which forms a valid signature tuple and groups empty strings together correctly.
- Single string: Handled trivially without branching, producing a single group of size 1.
- Identical strings / duplicate words: Grouped together since their frequency counts are identical; preserves relative encounter order as elements are appended sequentially.
- Tie-breaking: When two groups have the same length, `(-len(group), group[0])` breaks ties using standard lexicographical comparison of the first element.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group anagrams together using character frequency signatures."""
    groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
    base_ord = ord('a')

    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - base_ord] += 1
        groups[tuple(count)].append(s)

    result = list(groups.values())
    result.sort(key=lambda group: (-len(group), group[0]))
    return result
```
