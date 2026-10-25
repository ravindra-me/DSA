def longest_consecutive_sequence(nums: list[int]) -> int:
    """Return the length of the longest consecutive sequence in O(n) time."""
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only attempt to build sequences from their start
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            if current_streak > max_length:
                max_length = current_streak

    return max_length
