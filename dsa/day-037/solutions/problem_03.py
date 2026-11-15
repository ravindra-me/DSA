def radix_sort(nums: list[int]) -> list[int]:
    """Sorts non-negative integers using LSD Radix Sort."""
    if len(nums) <= 1:
        return list(nums)

    max_val = max(nums)
    if max_val == 0:
        return list(nums)

    current = list(nums)
    n = len(current)
    bits = max_val.bit_length()
    shift = 0
    radix = 256
    mask = 0xFF

    while shift < bits:
        count = [0] * radix
        output = [0] * n

        for num in current:
            digit = (num >> shift) & mask
            count[digit] += 1

        for i in range(1, radix):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            num = current[i]
            digit = (num >> shift) & mask
            count[digit] -= 1
            output[count[digit]] = num

        current = output
        shift += 8

    return current
