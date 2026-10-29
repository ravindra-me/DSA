# Solution 3: Coprime Component Groups

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** GCD & Prime Factorization Graph Reduction

## Approach

Connect each number to its prime factors in a Disjoint Set Union (DSU) structure. Since numbers sharing a common prime factor are connected, unioning each number with all of its prime factors implicitly connects all numbers that share any prime factor or chain of shared factors.

## Thought Process

A naive approach checks every pair $(i, j)$ and computes $\gcd(nums[i], nums[j])$, which takes $O(N^2 \log M)$ where $N \le 20000$ and $M \le 100000$. With $N = 20000$, $N^2 = 4 \times 10^8$ operations, which will exceed typical time limits.

Notice that $\gcd(a, b) > 1$ if and only if $a$ and $b$ share at least one prime factor $p$. Instead of connecting numbers directly to each other, we can view prime factors as intermediate hubs in a bipartite-like graph. For each number $x$, find its prime factors $p_1, p_2, \dots, p_k$ and union $x$ (or its first prime factor) with each of its prime factors in a Disjoint Set Union (DSU) data structure. Alternatively, we can just union all prime factors of $x$ together. Then, each number $x > 1$ belongs to the component of its prime factors. Finally, we count the number of elements in `nums` mapped to each root representative.

## Algorithm

1. Precompute or factorize on the fly each number $x \in \text{nums}$. Since $\max(nums) \le 100000$, we can precompute the smallest prime factor (SPF) for all numbers up to $\max(nums)$ using a sieve in $O(M \log \log M)$ time.
2. Initialize a Disjoint Set Union (DSU) data structure over all prime numbers up to $\max(nums)$ (or simply up to $\max(nums) + 1$).
3. For each number $x > 1$ in `nums`, find its distinct prime factors using the SPF array. Union the first prime factor with every other prime factor of $x$.
4. To compute the component sizes of the input numbers, find the root of the first prime factor for each $x > 1$ in `nums`, and tally counts in a hash map or frequency array.
5. Return the maximum count among all components. If no number has prime factors (e.g. all 1s), return 1 if `nums` is non-empty (as individual isolated 1s have component size 1), or 0 if empty (though constraints specify $N \ge 1$).

## Complexity Analysis

- **Time:** $O(M \log \log M + N \log M)$, where $M = \max(nums) \le 10^5$ and $N = \text{len}(nums)$. Sieve of Eratosthenes takes $O(M \log \log M)$, factorization takes $O(\log M)$ per number, and DSU operations with path compression take nearly $O(1)$ amortized time.
- **Space:** $O(M)$ to store the smallest prime factor (SPF) array and the DSU parent/rank arrays up to $M = \max(nums)$.

## Edge Cases

- Numbers equal to 1: 1 has no prime factors and can never have $\gcd > 1$ with any number. If all numbers are 1 or each number is coprime to all others, the maximum component size is 1.
- Single element list: Always returns 1 as that single element forms a component of size 1.
- Duplicate numbers: Duplicate values $> 1$ share identical prime factors and properly increment the component count.
- All elements sharing a common factor: All elements merge into a single component of size $N$.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from collections import Counter


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1


def largest_coprime_component(nums: list[int]) -> int:
    """Return the size of the largest connected component where edges exist when gcd > 1."""
    if not nums:
        return 0

    max_val = max(nums)
    if max_val <= 1:
        return 1

    # Sieve to compute the smallest prime factor (SPF) for each integer up to max_val
    spf = list(range(max_val + 1))
    for i in range(2, int(max_val**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_val + 1, i):
                if spf[j] == j:
                    spf[j] = i

    dsu = DSU(max_val + 1)

    def get_prime_factors(val: int) -> list[int]:
        factors: list[int] = []
        while val > 1:
            p = spf[val]
            factors.append(p)
            while val % p == 0:
                val //= p
        return factors

    # Union all prime factors of each number
    for num in nums:
        if num > 1:
            factors = get_prime_factors(num)
            first_factor = factors[0]
            for factor in factors[1:]:
                dsu.union(first_factor, factor)

    # Count the number of elements belonging to each prime component
    counts: Counter[int] = Counter()
    for num in nums:
        if num > 1:
            p = spf[num]
            root = dsu.find(p)
            counts[root] += 1

    if not counts:
        return 1

    return max(counts.values())
```
