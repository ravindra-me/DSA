def get_next(n: int) -> int:
    """Calculate the sum of squares of digits of n."""
    total_sum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total_sum += digit * digit
    return total_sum


def is_happy(n: int) -> bool:
    """Return True if n is a happy number, False otherwise."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
