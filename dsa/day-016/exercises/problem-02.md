# Problem 2: Group Anagrams by Signature

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Hashing composite keys / canonical representation | [Day 16: HashMap](../README.md) |

## Problem Statement

Given an array of strings `words`, group all anagrams together. An anagram is a word formed by rearranging the letters of another. Return the groups sorted in descending order of group size. Break ties between groups of equal size by sorting their elements alphabetically and comparing the first element of each group lexicographically.

## Input

`words: list[str]` - a list of lowercase English strings.

## Output

`list[list[str]]` - groups of anagrams ordered as described, with strings inside each group sorted alphabetically.

## Constraints

- 0 <= len(words) <= 10^4
- 0 <= len(words[i]) <= 100
- words[i] consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
```

["ate", "eat", "tea"] has size 3. ["nat", "tan"] has size 2. ["bat"] has size 1.

**Example 2**

```text
Input:  words = []
Output: []
```

Empty input produces empty output.

## Function Signature

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group anagrams together and sort groups according to specifications."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Compute a canonical key for each string (e.g. sorted characters or character frequency tuple) and use a HashMap to aggregate words with identical keys.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
