def find_nth_root(n: float, p: int, eps: float = 1e-7) -> float:
    """Return x such that x^p == n, accurate to within eps."""
    if p == 1:
        return float(n)

    low = 0.0
    high = max(1.0, float(n))

    # 80 iterations halves the interval by 2^80 (~1.2e24), well beyond IEEE 754 float precision
    for _ in range(80):
        mid = (low + high) / 2.0
        if mid**p < n:
            low = mid
        else:
            high = mid

    return (low + high) / 2.0
