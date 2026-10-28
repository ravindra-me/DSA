from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements in O(n) time using bucket sort."""
    counts = Counter(nums)
    n = len(nums)
    buckets: list[list[int]] = [[] for _ in range(n + 1)]
    
    for num, freq in counts.items():
        buckets[freq].append(num)
        
    result: list[int] = []
    for freq in range(n, 0, -1):
        if not buckets[freq]:
            continue
        buckets[freq].sort()
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
                
    return result
