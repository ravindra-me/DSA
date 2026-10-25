# Solution 2: Group Anagrams by Signature

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Hashing composite keys / canonical representation

## Approach

Group words using a canonical signature as the hash map key—either the sorted characters of each word or a 26-element character count tuple. Once all words are grouped, sort the elements within each group alphabetically, and then sort the groups themselves by descending length with ties broken lexicographically by the group's first element.

## Thought Process

Two words are anagrams if and only if they contain the exact same characters with identical frequencies. A naive approach might compare every pair of words by counting characters, taking $O(N^2 \cdot L)$ time, which is too slow for $N = 10^4$.

To improve this, we need a canonical representation for an anagram family that can act as a hash table key in $O(L)$ time per word. Two common representations exist:
1. Sorting the characters of the word: $O(L \log L)$. Since $L \le 100$, $L \log L$ is tiny ($\approx 660$ operations max).
2. A 26-element frequency tuple: $O(L)$ time.

Sorting the string is concise and extremely fast in Python's optimized C implementation of Timsort. We map each canonical signature to a list of original words using `collections.defaultdict(list)`.

Finally, we post-process the groups: each group must be sorted alphabetically, and the list of groups must be sorted by `(-len(group), group[0])` to satisfy the custom tie-breaking criteria.

## Algorithm

1. Initialize an empty hash map `groups = collections.defaultdict(list)` mapping canonical signatures to lists of words.
2. For each word in `words`, compute its canonical signature by sorting its characters into a string: `"".join(sorted(word))`.
3. Append the original word to `groups[signature]`.
4. Iterate through the values in `groups`, sorting the strings within each group in ascending alphabetical order.
5. Sort the list of groups using the key `(-len(group), group[0])` so that larger groups come first, and ties are broken lexicographically by the first word.
6. Return the resulting sorted list of groups.

## Complexity Analysis

- **Time:** $O(N \cdot L \log L + N \log N)$ where $N$ is the number of words and $L$ is the maximum length of a word. Grouping takes $O(N \cdot L \log L)$. Sorting within groups takes at most $O(N \log N)$, and sorting the groups takes $O(K \log K \cdot L)$ where $K \le N$ is the number of distinct groups.
- **Space:** $O(N \cdot L)$ auxiliary space to store the hash map and resulting grouped lists.

## Edge Cases

- Empty input list: handled immediately, returning an empty list `[]`.
- Empty strings: handled correctly since `"".join(sorted(""))` is `""`.
- Duplicate words: preserved and grouped together under the same anagram key.
- Tie-breaking: groups of equal size are correctly ordered by comparing their first elements lexicographically.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group anagrams together and sort groups according to specifications."""
    if not words:
        return []

    grouped: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        signature = "".join(sorted(word))
        grouped[signature].append(word)

    result: list[list[str]] = []
    for group in grouped.values():
        group.sort()
        result.append(group)

    result.sort(key=lambda g: (-len(g), g[0]))
    return result
```
