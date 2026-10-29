from collections import defaultdict

def count_subarrays_divisible(nums: list[int], k: int) -> int:
    """Return the number of continuous subarrays with sum divisible by k."""
    remainder_counts: dict[int, int] = defaultdict(int)
    remainder_counts[0] = 1
    
    running_sum = 0
    total_subarrays = 0
    
    for num in nums:
        running_sum += num
        rem = running_sum % k
        total_subarrays += remainder_counts[rem]
        remainder_counts[rem] += 1
        
    return total_subarrays
