# Problem 2: Group Anagrams

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Character Frequency Signatures and Hashing | [Day 3: Strings](../README.md) |

## Problem Statement

Given a list of strings `words`, group the anagrams together. You may return the answer in any order.

An **anagram** is a word formed by rearranging the letters of another word, using all the original letters exactly once. All strings consist of lowercase English letters.

## Input

`words: list[str]` — a list of strings.

## Output

`list[list[str]]` — groups of anagrams. The outer list and inner lists can be in any order.

## Constraints

- 1 <= len(words) <= 10^4
- 0 <= len(words[i]) <= 100
- `words[i]` consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

"eat", "tea", and "ate" are anagrams of each other. "tan" and "nat" form another group. "bat" is in its own group.

**Example 2**

```text
Input:  words = [""]
Output: [[""]]
```

Edge case: a single empty string forms a single group containing the empty string.

**Example 3**

```text
Input:  words = ["a"]
Output: [["a"]]
```

A single character forms a single group.

## Function Signature

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group a list of strings into anagram clusters."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Map each word to a canonical key—either a sorted string or a 26-element tuple of character frequency counts—and collect anagrams using a hash table. Aim for $O(N \cdot K)$ time where $N$ is word count and $K$ is maximum word length.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
