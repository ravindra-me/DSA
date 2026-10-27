# Solution 5: Minimum Genetic Mutation

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** HashSet for graph search state verification and visited tracking

## Approach

This problem can be modeled as finding the shortest path in an unweighted graph where each valid gene string is a node and an edge exists between two genes if they differ by exactly one character. We use Breadth-First Search (BFS) combined with a `HashSet` representing the bank for $O(1)$ valid gene lookup and a `visited` `HashSet` (or by removing visited genes from the bank set) to prevent infinite loops and redundant exploration.

## Thought Process

Since we want the minimum number of mutations (shortest path in an unweighted graph), BFS is the natural fit. A naive approach might generate all possible strings or check every string in the bank against the current gene repeatedly ($O(N)$ lookup each step), leading to inefficient transitions. By converting the bank into a `HashSet`, we can instantly verify whether a generated 1-mutation neighbor exists in the bank. Since gene strings are short (length 8) and the alphabet size is small ($|\Sigma| = 4$), generating all 8 * 3 = 24 possible 1-mutation neighbors for a gene and looking them up in the `HashSet` takes $O(L \cdot |\Sigma|) = O(1)$ time per node.

## Algorithm

1. Convert `bank` into a `HashSet` called `bank_set`. If `end_gene` is not in `bank_set`, return -1 immediately.
2. Initialize a BFS queue `queue = deque([(start_gene, 0)])` storing tuples of `(current_gene, mutations_count)`.
3. Initialize a `visited` set containing `start_gene` to prevent revisiting states.
4. While `queue` is not empty, pop `(curr, depth)`.
5. If `curr == end_gene`, return `depth`.
6. For each character position $i$ from 0 to 7 and each character $c$ in `['A', 'C', 'G', 'T']` diffing from `curr[i]`:
7. Construct the mutated gene candidate `neighbor = curr[:i] + c + curr[i+1:]`.
8. If `neighbor` is in `bank_set` and not in `visited`, add `neighbor` to `visited` and append `(neighbor, depth + 1)` to `queue`.
9. If the queue becomes empty without reaching `end_gene`, return -1.

## Complexity Analysis

- **Time:** $O(N \cdot L^2 \cdot |\Sigma|)$ where $N$ is the number of genes in the bank, $L = 8$ is the length of a gene string, and $|\Sigma| = 4$ is the alphabet size. Since $L$ and $|\Sigma|$ are constants, the search takes $O(N)$ time.
- **Space:** $O(N \cdot L) = O(N)$ to store the bank set, visited set, and queue in memory.

## Edge Cases

- `end_gene` is not present in `bank`: handled early by checking if `end_gene` is in `bank_set`, returning -1.
- `start_gene` is already `end_gene`: returned directly as 0 mutations.
- `bank` is empty: returns -1 immediately.
- Unreachable `end_gene` despite being in `bank`: BFS finishes without finding a valid path and returns -1.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import deque

def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    """Return minimum mutations from start_gene to end_gene via bank, or -1."""
    bank_set = set(bank)
    if end_gene not in bank_set:
        return -1
    
    queue = deque([(start_gene, 0)])
    visited = {start_gene}
    gene_chars = ['A', 'C', 'G', 'T']
    
    while queue:
        curr, depth = queue.popleft()
        if curr == end_gene:
            return depth
        
        for i in range(len(curr)):
            original_char = curr[i]
            for c in gene_chars:
                if c == original_char:
                    continue
                neighbor = curr[:i] + c + curr[i+1:]
                if neighbor in bank_set and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
    return -1
```
