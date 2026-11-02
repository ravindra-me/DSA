from collections import Counter

def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    """Counts the number of contiguous subarrays having exactly k distinct integers."""
    def at_most_k(k_val: int) -> int:
        if k_val <= 0:
            return 0
        
        freq = Counter()
        left = 0
        total_subarrays = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while len(freq) > k_val:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            total_subarrays += (right - left + 1)
            
        return total_subarrays

    return at_most_k(k) - at_most_k(k - 1)
