def first_missing_positive(nums: list[int]) -> int:
    """Return the smallest positive integer missing from nums.

    Runs in O(n) time and O(1) auxiliary space via in-place cyclic indexing.
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
