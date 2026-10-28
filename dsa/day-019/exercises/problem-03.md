# Problem 3: Group Anagrams by Count Signature

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | canonical frequency signatures as dictionary keys | [Day 19: Frequency Counting](../README.md) |

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order within groups, but each group of words should preserve their relative encounter order. The outer list should be sorted by the length of each group in descending order; if two groups have the same size, break ties by comparing their first element lexicographically.

## Input

A list of strings `strs`.

## Output

A list of lists of strings grouped by anagrams and sorted as specified.

## Constraints

- 1 <= len(strs) <= 10^4
- 0 <= len(strs[i]) <= 100
- `strs[i]` consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

Group ["eat", "tea", "ate"] has size 3. ["tan", "nat"] has size 2. ["bat"] has size 1.

**Example 2**

```text
Input:  strs = [""]
Output: [[""]]
```

A single empty string forms a single group.

**Example 3**

```text
Input:  strs = ["a"]
Output: [["a"]]
```

Single character string forms a single group.

## Function Signature

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group anagrams together using character frequency signatures."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Map each string to a tuple representing its 26-character frequency count. Group strings having identical tuples in a hash map, then sort the groups according to the problem specification.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
