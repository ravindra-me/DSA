def longest_consecutive(nums: list[int]) -> int:
    """Return length of longest consecutive elements sequence in O(N) time."""
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Check if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            if current_length > max_length:
                max_length = current_length

    return max_length
