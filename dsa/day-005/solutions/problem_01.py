def reverse_integer(x: int) -> int:
    """Reverses digits of a 32-bit signed integer mathematically."""
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    sign = -1 if x < 0 else 1
    n = abs(x)
    reversed_num = 0
    max_limit = -INT_MIN if sign == -1 else INT_MAX

    while n > 0:
        digit = n % 10
        if reversed_num > (max_limit - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num
