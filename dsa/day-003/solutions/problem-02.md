# Solution 2: Group Anagrams

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Character Frequency Signatures and Hashing

## Approach

Two words are anagrams if and only if they have identical character counts. We can map each word to a canonical representation—either a sorted version of the string or a 26-element tuple representing letter frequencies—and use that representation as a key in a hash map (`collections.defaultdict(list)`). The values of the hash map yield the anagram groups.

## Thought Process

A brute-force solution would compare every word against every other word to check if they are anagrams. Comparing two words of length $L$ takes $O(L)$ or $O(L \log L)$ time, leading to an overall $O(N^2 \cdot L)$ time complexity for $N$ words. With $N = 10^4$, $N^2 = 10^8$ operations, which risks timing out or being unnecessarily slow.

To optimize, observe that 'being an anagram' is an equivalence relation. In any equivalence relation problem, canonicalization allows grouping in $O(N)$ hash-table lookups. Each word can be reduced to a canonical signature that is invariant under letter permutations.

There are two common canonical signatures:
1. **Sorted string signature**: Sorting each word produces identical strings for anagrams (e.g., `"eat"`, `"tea"`, `"ate"` all become `"aet"`). This takes $O(L \log L)$ per word.
2. **Frequency count tuple**: Since all strings consist of lowercase English letters (`'a'` to `'z'`), we can count occurrences of each character into a fixed-size array/tuple of length 26. This takes $O(L)$ per word.

Given $L \le 100$, either signature is very fast. Using the 26-element frequency tuple achieves strictly $O(N \cdot L)$ runtime. In Python, tuples are hashable and can be used directly as dictionary keys.

## Algorithm

1. Initialize an empty hash map `groups = collections.defaultdict(list)`.
2. For each word in `words`, compute its character count signature: create an array of size 26 initialized to 0.
3. Iterate through the characters of the word, incrementing the count at index `ord(char) - ord('a')`.
4. Convert the count array into a hashable tuple and append the word to `groups[tuple(count)]`.
5. Return all values in `groups` as a list of lists.

## Complexity Analysis

- **Time:** $O(N \cdot L)$ where $N$ is the number of words and $L$ is the maximum length of a word. For each word, counting characters and converting a 26-element list to a tuple takes $O(L + 26) = O(L)$ time.
- **Space:** $O(N \cdot L)$ to store all words and their canonical tuple keys inside the hash map.

## Edge Cases

- Single empty string `[""]`: The frequency count is all zeros; it forms a single group `[[""]]`.
- Multiple empty strings `["", ""]`: Both map to the all-zero signature and group together into `[["", ""]]`.
- Duplicate words `["a", "a"]`: Identical words share the same frequency signature and are placed in the same group.
- Single-character words `["a"]`: Forms a single group with length 1.
- No shared anagrams: Every word produces a unique signature, yielding $N$ groups of size 1.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group a list of strings into anagram clusters."""
    groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
    ord_a = ord("a")

    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord_a] += 1
        groups[tuple(count)].append(word)

    return list(groups.values())
```
