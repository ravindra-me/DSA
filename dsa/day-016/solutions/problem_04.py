from collections import defaultdict


def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """Return the count of continuous subarrays with sum divisible by k."""
    remainder_counts: dict[int, int] = defaultdict(int)
    remainder_counts[0] = 1
    
    running_sum = 0
    result = 0
    
    for num in nums:
        running_sum = (running_sum + num) % k
        result += remainder_counts[running_sum]
        remainder_counts[running_sum] += 1
        
    return result
