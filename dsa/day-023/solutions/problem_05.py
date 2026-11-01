def minimum_xor_sum(nums1: list[int], nums2: list[int]) -> int:
    """Calculate the minimum XOR sum using bitmask dynamic programming."""
    n = len(nums1)
    num_states = 1 << n
    dp = [float('inf')] * num_states
    dp[0] = 0
    
    for mask in range(num_states):
        i = mask.bit_count()
        if i == n:
            continue
        
        val1 = nums1[i]
        for j in range(n):
            if not (mask & (1 << j)):
                next_mask = mask | (1 << j)
                cost = dp[mask] + (val1 ^ nums2[j])
                if cost < dp[next_mask]:
                    dp[next_mask] = cost
                    
    return int(dp[num_states - 1])
