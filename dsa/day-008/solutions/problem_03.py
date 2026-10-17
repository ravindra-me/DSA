def longest_duplicate_substring_length(s: str) -> int:
    """Return the maximum length of a duplicate substring in s."""
    n = len(s)
    if n <= 1:
        return 0

    nums = [ord(c) - ord("a") for c in s]
    base = 31
    mod1 = 1_000_000_007
    mod2 = 1_000_000_009

    def has_duplicate(length: int) -> bool:
        h1, h2 = 0, 0
        power1, power2 = 1, 1
        for i in range(length):
            h1 = (h1 * base + nums[i]) % mod1
            h2 = (h2 * base + nums[i]) % mod2
            if i < length - 1:
                power1 = (power1 * base) % mod1
                power2 = (power2 * base) % mod2

        seen = {(h1, h2)}
        for i in range(length, n):
            h1 = (h1 - nums[i - length] * power1) % mod1
            h1 = (h1 * base + nums[i]) % mod1

            h2 = (h2 - nums[i - length] * power2) % mod2
            h2 = (h2 * base + nums[i]) % mod2

            pair = (h1, h2)
            if pair in seen:
                return True
            seen.add(pair)

        return False

    low, high = 1, n - 1
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if has_duplicate(mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best
