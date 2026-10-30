from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    """Count the number of contiguous subarrays summing to k."""
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1
    
    current_sum = 0
    total_subarrays = 0
    
    for num in nums:
        current_sum += num
        target_prefix = current_sum - k
        if target_prefix in prefix_counts:
            total_subarrays += prefix_counts[target_prefix]
        prefix_counts[current_sum] += 1
        
    return total_subarrays
