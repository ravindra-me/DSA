class Solution:
    pass

def max_min_product(nums: list[int]) -> int:
    """Calculates the maximum min-product among all non-empty subarrays modulo 10^9 + 7."""
    MOD = 10**9 + 7
    n = len(nums)
    
    # Precompute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
        
    max_product = 0
    stack: list[int] = []  # Monotonic increasing stack storing indices
    
    for i in range(n + 1):
        # Use 0 as a sentinel value at index n
        current_val = nums[i] if i < n else 0
        
        while stack and nums[stack[-1]] > current_val:
            idx = stack.pop()
            min_val = nums[idx]
            
            right_bound = i - 1
            left_bound = stack[-1] + 1 if stack else 0
            
            total_sum = prefix[right_bound + 1] - prefix[left_bound]
            max_product = max(max_product, min_val * total_sum)
            
        stack.append(i)
        
    return max_product % MOD
