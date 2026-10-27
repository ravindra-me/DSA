# Problem 5: Minimum Genetic Mutation

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | HashSet for graph search state verification and visited tracking | [Day 18: HashSet](../README.md) |

## Problem Statement

A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `start_gene` to a gene string `end_gene` where one mutation is defined as changing a single character in the gene string.

- For example, `"AACCGGTT" --> "AACCGGTA"` is 1 mutation.

There is also a gene bank `bank` that records all valid gene mutations. A gene must be in `bank` to make it a valid gene string during mutations.

Given the two gene strings `start_gene` and `end_gene` and the gene bank `bank`, return the **minimum number of mutations** needed to mutate from `start_gene` to `end_gene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

## Input

`start_gene: str`, `end_gene: str`, `bank: list[str]`.

## Output

`int` - the minimum number of valid mutations, or `-1` if impossible.

## Constraints

- len(start_gene) == len(end_gene) == 8
- 0 <= len(bank) <= 100
- bank[i].length == 8
- start_gene, end_gene, and bank[i] consist of only ['A', 'C', 'G', 'T']

## Examples

**Example 1**

```text
Input:  start_gene = "AACCGGTT", end_gene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
```

Single mutation directly to bank entry.

**Example 2**

```text
Input:  start_gene = "AACCGGTT", end_gene = "AAACGGTA", bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
Output: 2
```

"AACCGGTT" -> "AACCGGTA" -> "AAACGGTA" takes 2 mutations.

**Example 3**

```text
Input:  start_gene = "AAAAACCC", end_gene = "AACCCCCC", bank = ["AAAACCCC", "AAACCCCC"]
Output: -1
```

end_gene is not in bank, so it cannot be reached.

## Function Signature

```python
def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    """Return minimum mutations from start_gene to end_gene via bank, or -1."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use BFS with a HashSet representation of the bank for O(1) validity checks and another HashSet for visited states to avoid cycles.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
