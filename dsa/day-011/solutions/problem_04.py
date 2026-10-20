def find_length(nums1: list[int], nums2: list[int]) -> int:
    """Finds the maximum length of a contiguous subarray appearing in both arrays."""
    # Optimization: ensure nums2 is the shorter array to minimize memory
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums2)
    dp = [0] * (m + 1)
    max_len = 0

    for val1 in nums1:
        for j in range(m, 0, -1):
            if val1 == nums2[j - 1]:
                dp[j] = dp[j - 1] + 1
                if dp[j] > max_len:
                    max_len = dp[j]
            else:
                dp[j] = 0

    return max_len
