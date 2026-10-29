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
